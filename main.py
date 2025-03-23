import streamlit as st
import pandas as pd
import easyocr
from PIL import Image
import re
import os
import requests
from datetime import date
from io import BytesIO

# Config da página
st.set_page_config(page_title="Painel de Transporte", page_icon="🧾", layout="wide")

CSV_FILE = "abastecimentos.csv"

# Garante que o arquivo existe
if not os.path.exists(CSV_FILE):
    df_init = pd.DataFrame(columns=["data", "litros", "valor", "local", "link_nota"])
    df_init.to_csv(CSV_FILE, index=False)

st.title("📸 Leitor Inteligente de Cupons Fiscais")

imagem = st.file_uploader("Envie a foto do cupom fiscal", type=["jpg", "jpeg", "png"])

def extrair_qrcode_da_imagem(file):
    api_url = "https://api.qrserver.com/v1/read-qr-code/"
    files = {'file': file}
    try:
        resposta = requests.post(api_url, files=files, timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            conteudo = dados[0]['symbol'][0]['data']
            return conteudo
    except:
        return None
    return None

if imagem:
    st.image(imagem, caption="Cupom enviado", use_container_width=True)

    with st.spinner("Lendo QR Code da nota fiscal..."):
        qr_resultado = extrair_qrcode_da_imagem(imagem)

    # Valores padrão
    data_extraida = date.today().strftime("%Y-%m-%d")
    litros_extraido = 0.0
    valor_extraido = 0.0

    if qr_resultado and "http" in qr_resultado:
        st.success("QR Code lido com sucesso!")
        st.markdown(f"🔗 [Acessar nota fiscal]({qr_resultado})")
    else:
        st.warning("QR Code não encontrado. Utilizando OCR como plano B...")

        # OCR via EasyOCR
        reader = easyocr.Reader(['pt'], gpu=False)
        img = Image.open(imagem)
        resultado = reader.readtext(img, detail=0, paragraph=True)
        texto_lido = "\n".join(resultado)

        st.markdown("### Texto lido via OCR:")
        st.code(texto_lido)

        # Data
        datas = re.findall(r"\d{2}/\d{2}/\d{4}", texto_lido)
        if datas:
            data_extraida = datas[-1]

        # Valor total
        palavras_chave_valor = ["total", "valor total", "total a pagar", "valor pago", "pagamento", "à pagar", "total final", "vl.total"]
        palavras_ruins = ["hora", "troco", "cpf", "cnpj", "subtotal"]
        for linha in resultado:
            linha_min = linha.lower()
            if any(bad in linha_min for bad in palavras_ruins):
                continue
            if any(chave in linha_min for chave in palavras_chave_valor):
                if ':' in linha_min:
                    continue
                numeros = re.findall(r"\d+[.,]\d{2}", linha)
                if numeros:
                    valor_extraido = float(numeros[-1].replace(",", "."))
                    break

        # Plano B para valor
        if valor_extraido == 0.0:
            valores = re.findall(r"\d+[.,]\d{2}", texto_lido)
            valores = [v for v in valores if ":" not in v]
            valores_float = [float(v.replace(",", ".")) for v in valores]
            valor_extraido = max(valores_float) if valores_float else 0.0

        # Litros
        padrao_litros = re.findall(r"(\d+[.,]\d{3})\s*(l|litros)", texto_lido.lower())
        if padrao_litros:
            litros_bruto = padrao_litros[0][0]
            litros_extraido = float(litros_bruto.replace(",", "."))

    # Salva automaticamente os dados
    novo = {
        "data": data_extraida,
        "litros": litros_extraido,
        "valor": valor_extraido,
        "local": "",
        "link_nota": qr_resultado if qr_resultado else ""
    }

    df = pd.read_csv(CSV_FILE)
    df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

    st.success("✅ Cupom registrado automaticamente!")

# Seção: Abastecimentos Registrados
st.markdown("---")
st.subheader("⛽ Abastecimentos Registrados")
df = pd.read_csv(CSV_FILE)

if df.empty:
    st.info("Nenhum registro ainda.")
else:
    st.dataframe(df[::-1], use_container_width=True)

# Seção: Editar registro
st.markdown("---")
st.subheader("✏️ Editar Registro Existente")

df = pd.read_csv(CSV_FILE)
if not df.empty:
    opcoes = [f"{i} - {row['data']} | R$ {row['valor']} | {row['litros']} L" for i, row in df.iterrows()]
    escolha = st.selectbox("Selecione um registro para editar:", opcoes)

    if escolha:
        idx = int(escolha.split(" - ")[0])
        registro = df.loc[idx]

        with st.form("editar_registro"):
            nova_data = st.text_input("Data", registro["data"])
            novos_litros = st.number_input("Litros abastecidos", value=registro["litros"], format="%.3f")
            novo_valor = st.number_input("Valor total (R$)", value=registro["valor"], format="%.2f")
            novo_local = st.text_input("Local", registro["local"])
            novo_link = st.text_input("Link da Nota", registro["link_nota"])

            salvar = st.form_submit_button("💾 Salvar Edição")

            if salvar:
                df.at[idx, "data"] = nova_data
                df.at[idx, "litros"] = novos_litros
                df.at[idx, "valor"] = novo_valor
                df.at[idx, "local"] = novo_local
                df.at[idx, "link_nota"] = novo_link
                df.to_csv(CSV_FILE, index=False)
                st.success("✅ Registro atualizado com sucesso!")
