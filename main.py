import streamlit as st
import pandas as pd
import pytesseract
from PIL import Image
import re
import os
from datetime import date

# Configuração da página
st.set_page_config(page_title="Painel de Transporte", page_icon="🧾", layout="wide")

CSV_FILE = "abastecimentos.csv"

# Garante que o arquivo exista
if not os.path.exists(CSV_FILE):
    df_init = pd.DataFrame(columns=["data", "litros", "valor", "local"])
    df_init.to_csv(CSV_FILE, index=False)

st.title("🧾 Upload de Cupom Fiscal")

# Upload da imagem
imagem = st.file_uploader("Envie uma foto do cupom fiscal", type=["png", "jpg", "jpeg"])

if imagem:
    # Exibe a imagem enviada
    st.image(imagem, caption="Cupom enviado", use_column_width=True)

    # Converte para imagem PIL
    img = Image.open(imagem)

    # Leitura com OCR
    texto = pytesseract.image_to_string(img, lang='por')

    st.markdown("### 🧠 Texto lido do cupom:")
    st.code(texto)

    # Tenta extrair a data (formato DD/MM/YYYY)
    datas = re.findall(r"\d{2}/\d{2}/\d{4}", texto)
    data_extraida = datas[0] if datas else date.today().strftime("%Y-%m-%d")

    # Tenta extrair os valores monetários (R$)
    valores = re.findall(r"\d+[.,]\d{2}", texto)
    valores_float = [float(v.replace(",", ".")) for v in valores]
    valor_extraido = max(valores_float) if valores_float else 0.0

    # Exibe informações reconhecidas
    st.markdown("### 📋 Informações extraídas:")
    st.write(f"🗓️ Data: `{data_extraida}`")
    st.write(f"💰 Valor total: `R$ {valor_extraido:,.2f}`")

    if st.button("💾 Salvar no sistema"):
        novo = {
            "data": data_extraida,
            "litros": 0.0,  # Ainda não extraímos litros
            "valor": valor_extraido,
            "local": ""
        }

        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)

        st.success("✅ Abastecimento salvo com sucesso!")

st.markdown("---")
st.subheader("⛽ Abastecimentos Registrados")
df = pd.read_csv(CSV_FILE)

if df.empty:
    st.info("Nenhum abastecimento registrado ainda.")
else:
    st.dataframe(df[::-1], use_container_width=True)
