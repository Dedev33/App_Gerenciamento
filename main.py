import streamlit as st
import pandas as pd
import easyocr
from PIL import Image
import re
import os
from datetime import date

# Configuração da página
st.set_page_config(page_title="Painel de Transporte", page_icon="🧾", layout="wide")

CSV_FILE = "abastecimentos.csv"

if not os.path.exists(CSV_FILE):
    df_init = pd.DataFrame(columns=["data", "valor", "local"])
    df_init.to_csv(CSV_FILE, index=False)

st.title("📸 Leitor de Cupons Fiscais (OCR)")

imagem = st.file_uploader("Envie uma imagem do cupom fiscal", type=["jpg", "jpeg", "png"])

if imagem:
    st.image(imagem, caption="Cupom enviado", use_container_width=True)
    reader = easyocr.Reader(['pt'], gpu=False)
    texto = reader.readtext(Image.open(imagem), detail=0, paragraph=True)
    texto_unido = "\n".join(texto)

    st.markdown("### Texto lido:")
    st.code(texto_unido)

    # Extração da data
    datas = re.findall(r"\d{2}/\d{2}/\d{4}", texto_unido)
    data_detectada = datas[-1] if datas else date.today().strftime("%Y-%m-%d")

    # Extração do valor
    valores = re.findall(r"\d+[.,]\d{2}", texto_unido)
    valores_float = [float(v.replace(",", ".")) for v in valores if ":" not in v]
    valor_detectado = max(valores_float) if valores_float else 0.0

    # Extração do local
    local_linha = next((linha for linha in texto if any(palavra in linha.lower() for palavra in ["posto", "rodovia", "avenida", "bairro", "rua"])), "")
    local_detectado = local_linha.strip()

    # Formulário de confirmação
    with st.form("confirmar_registro"):
        st.subheader("✅ Confirmar Registro")
        data_final = st.text_input("Data", value=data_detectada)
        valor_final = st.number_input("Valor Total (R$)", value=valor_detectado, format="%.2f")
        local_final = st.text_input("Local", value=local_detectado)
        confirmar = st.form_submit_button("Aprovar e Salvar Registro")

        if confirmar:
            df = pd.read_csv(CSV_FILE)
            novo = {"data": data_final, "valor": valor_final, "local": local_final}
            df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
            df.to_csv(CSV_FILE, index=False)
            st.success("Registro salvo com sucesso!")

# Exibição de registros
st.markdown("---")
st.subheader("⛽ Registros de Abastecimento")
df = pd.read_csv(CSV_FILE)

if df.empty:
    st.info("Nenhum registro ainda.")
else:
    st.dataframe(df[::-1], use_container_width=True)

    st.markdown("### ✏️ Editar ou 🗑️ Deletar Registro")
    opcoes = [f"{i} - {row['data']} | R$ {row['valor']} | {row['local']}" for i, row in df.iterrows()]
    escolha = st.selectbox("Escolha o registro:", opcoes)

    if escolha:
        idx = int(escolha.split(" - ")[0])
        registro = df.loc[idx]

        with st.form("editar_ou_deletar"):
            nova_data = st.text_input("Data", value=registro["data"])
            novo_valor = st.number_input("Valor (R$)", value=float(registro["valor"]), format="%.2f")
            novo_local = st.text_input("Local", value=registro["local"])
            editar = st.form_submit_button("💾 Salvar Alterações")
            deletar = st.form_submit_button("🗑️ Deletar Registro")

            if editar:
                df.at[idx, "data"] = nova_data
                df.at[idx, "valor"] = novo_valor
                df.at[idx, "local"] = novo_local
                df.to_csv(CSV_FILE, index=False)
                st.success("Registro atualizado!")

            if deletar:
                df = df.drop(index=idx)
                df.to_csv(CSV_FILE, index=False)
                st.success("Registro deletado com sucesso!")
