import streamlit as st

st.set_page_config(
    page_title="Sistema Scania",
    page_icon="🚛",
    layout="wide"
)

st.markdown("""
    <style>
    html, body, [class*="css"]  {
        background-color: #0B0F1A;
        color: #FFFFFF;
        font-family: 'Segoe UI', sans-serif;
    }
    .block-container {
        padding: 2rem;
    }
    .scania-card {
        background-color: #141B2D;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
        text-align: center;
        margin-bottom: 20px;
        color: #FFFFFF;
    }
    .scania-title {
        font-size: 32px;
        font-weight: bold;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 30px;
    }
    .scania-label {
        font-size: 18px;
        color: #CCCCCC;
    }
    .scania-value {
        font-size: 26px;
        font-weight: bold;
        color: #E60012;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='scania-title'>🚛 Sistema de Controle - Transporte Scania</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='scania-card'><div class='scania-label'>Lucro Bruto</div><div class='scania-value'>R$ 15.800,00</div></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='scania-card'><div class='scania-label'>Lucro Líquido</div><div class='scania-value'>R$ 10.320,00</div></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='scania-card'><div class='scania-label'>Gastos com Combustível</div><div class='scania-value'>R$ 2.760,00</div></div>", unsafe_allow_html=True)
