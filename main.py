import streamlit as st
import pandas as pd
import easyocr
from PIL import Image
import re
import os
from datetime import date

# Config da página
st.set_page_config(page_title="Painel de Transporte", page_icon="🧾", layout="wide")

CSV_FILE = "abastecimentos.csv"

# Garante que o arquivo exista
if not os.path.exists(CSV_FILE):
    df_init = pd.DataFrame(columns=["data", "litros", "valor", "local"])
    df_init.to_csv(CSV_FILE, index=False)

st.title("📸 Leitura de Cupom Fiscal")

# Upload da imagem
imagem = st.file_uploader("Envie uma foto do cupom (jpg, png)", type=["jpg", "jpeg", "png"])

if imagem:
    st.image(imagem, caption="Cupom enviado", use_container_width=True)

    # Inicializa o leitor OCR
    reader = easyocr.Reader(['pt'], gpu=False)
    img = Image.open(imagem)
    resultado = reader.readtext(img, detail=0, paragraph=True)

    texto_lido = "\n".join(resultado)

    st.markdown("### 🧠 Texto lido do cupom:")
    st.code(texto_lido)

    # 🔎 Buscando a data no texto (formato DD/MM/YYYY)
    datas = re.findall(r"\d{2}/\d{2}/\d{4}", texto_lido)
    data_extraida = datas[0] if datas else date.today().strftime("%Y-%m-%d")

    # 🔎 Buscando o valor correto com base em palavras-chave
    valor_extraido = 0.0
    palavras_chave = ["total", "valor total", "total a pagar", "valor pago", "pago", "pagar"]

    for linha in resultado:
        linha_min = linha.lower()
        if any(palavra in linha_min for palavra in palavras_chave):
            numeros = re.findall(r"\d+[.,]\d{2}", linha)
            if numeros:
                valor_extraido = float(numeros[-1].replace(",", "."))
                break

    # Plano B (caso não encontre por palavras-chave)
    if valor_extraido == 0.0:
        valores = re.findall(r"\d+[.,]\d{2}", texto_lido)
        valores_float = [float(v.replace(",", ".")) for v in valores]
        valor_extraido = max(valores_float) if valores_float else 0.0

    # Exibindo o que foi extraído
    st.markdown("### 📋 Informações extraídas:")
    st.write(f"🗓️ Data: `{data_extraida}`")
    st.write(f"💰 Valor total: `R$ {valor_extraido:,.2f}`")

    if st.button("💾 Salvar no sistema"):
        novo = {
            "data": data_extraida,
            "litros": 0.0,
            "valor": valor_extraido,
            "local": ""
        }

        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)

        st.success("✅ Cupom salvo com sucesso!")

st.markdown("---")
st.subheader("⛽ Abastecimentos Registrados")
df = pd.read_csv(CSV_FILE)

if df.empty:
    st.info("Nenhum abastecimento registrado ainda.")
else:
    st.dataframe(df[::-1], use_container_width=True)
