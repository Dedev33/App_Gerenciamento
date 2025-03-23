import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Sistema Scania",
    page_icon="🚛",
    layout="wide"
)

# Estilo visual atualizado (fundo escuro total + Scania Style)
st.markdown("""
    <style>
    html, body, [class*="css"] {
        background-color: #0B0F1A;
        color: #FFFFFF;
        font-family: 'Segoe UI', sans-serif;
    }

    .block-container {
        padding: 2rem;
        max-width: 100%;
    }

    .scania-title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
        color: white;
    }

    .scania-icon {
        text-align: center;
        font-size: 50px;
        margin-bottom: 10px;
    }

    .scania-card {
        background-color: #111827;
        border-radius: 20px;
        padding: 30px 20px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.6);
        text-align: center;
        margin-bottom: 20px;
    }

    .scania-label {
        font-size: 18px;
        color: #9CA3AF;
        margin-bottom: 8px;
    }

    .scania-value {
        font-size: 28px;
        font-weight: bold;
        color: #E60012;
    }
    </style>
""", unsafe_allow_html=True)

# Ícone e título
st.markdown("<div class='scania-icon'>🚛</div>", unsafe_allow_html=True)
st.markdown("<div class='scania-title'>Sistema de Controle • Transporte Scania</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Layout com 3 colunas
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class='scania-card'>
            <div class='scania-label'>Lucro Bruto</div>
            <div class='scania-value'>R$ 15.800,00</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class='scania-card'>
            <div class='scania-label'>Lucro Líquido</div>
            <div class='scania-value'>R$ 10.320,00</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class='scania-card'>
            <div class='scania-label'>Gastos com Combustível</div>
            <div class='scania-value'>R$ 2.760,00</div>
        </div>
    """, unsafe_allow_html=True)

