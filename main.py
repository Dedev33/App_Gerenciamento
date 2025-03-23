import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Sistema de Controle",
    page_icon="🧾",
    layout="wide"
)

# Estilo visual refinado e elegante
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

    .banner {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }

    .banner img {
        max-width: 320px;
        border-radius: 16px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.6);
    }

    .app-title {
        font-size: 34px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 30px;
        color: white;
    }

    .card {
        background-color: #111827;
        border-radius: 20px;
        padding: 30px 20px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.6);
        text-align: center;
        margin-bottom: 20px;
    }

    .label {
        font-size: 18px;
        color: #9CA3AF;
        margin-bottom: 8px;
    }

    .value {
        font-size: 28px;
        font-weight: bold;
        color: #E60012;
    }
    </style>
""", unsafe_allow_html=True)

# Banner com imagem externa
st.markdown('<div class="banner"><img src="https://raw.githubusercontent.com/Dedev33/App_Gerenciamento/main/banner.jpg" alt="Hero Banner"></div>', unsafe_allow_html=True)

# Título principal
st.markdown('<div class="app-title">Sistema de Controle de Transporte</div>', unsafe_allow_html=True)

# Cartões com métricas
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class='card'>
            <div class='label'>Lucro Bruto</div>
            <div class='value'>R$ 15.800,00</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class='card'>
            <div class='label'>Lucro Líquido</div>
            <div class='value'>R$ 10.320,00</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class='card'>
            <div class='label'>Gastos com Combustível</div>
            <div class='value'>R$ 2.760,00</div>
        </div>
    """, unsafe_allow_html=True)
