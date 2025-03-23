import streamlit as st
import pandas as pd
import os
from datetime import date

# Config da página
st.set_page_config(
    page_title="Painel de Transporte",
    page_icon="🧾",
    layout="wide"
)

# Arquivo de dados
CSV_FILE = "abastecimentos.csv"

# Cria o arquivo se não existir
if not os.path.exists(CSV_FILE):
    df_init = pd.DataFrame(columns=["data", "litros", "valor", "local"])
    df_init.to_csv(CSV_FILE, index=False)

# Formulário
with st.form("form_abastecimento"):
    st.subheader("➕ Registrar Abastecimento")

    col1, col2 = st.columns(2)

    with col1:
        data_abastecimento = st.date_input("Data", value=date.today())
        litros = st.number_input("Litros abastecidos", min_value=0.0, step=1.0, format="%.2f")

    with col2:
        valor = st.number_input("Valor total (R$)", min_value=0.0, step=1.0, format="%.2f")
        local = st.text_input("Local (opcional)")

    submitted = st.form_submit_button("Salvar")

    if submitted:
        novo_registro = {
            "data": data_abastecimento.strftime("%Y-%m-%d"),
            "litros": litros,
            "valor": valor,
            "local": local
        }

        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, pd.DataFrame([novo_registro])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)

        st.success("✅ Abastecimento salvo com sucesso!")

# Mostrar registros (opcional nesta etapa)
st.markdown("---")
st.subheader("⛽ Abastecimentos Registrados")

df = pd.read_csv(CSV_FILE)

if df.empty:
    st.info("Nenhum abastecimento registrado ainda.")
else:
    st.dataframe(df[::-1], use_container_width=True)
