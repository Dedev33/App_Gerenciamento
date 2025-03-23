import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Painel de Transporte",
    page_icon="🧾",
    layout="wide"
)

# Estilos com base no layout de referência
st.markdown("""
    <style>
    html, body, [class*="css"] {
        background: url('https://raw.githubusercontent.com/Dedev33/App_Gerenciamento/main/banner.jpg.jpeg') no-repeat center center fixed;
        background-size: cover;
        font-family: 'Segoe UI', sans-serif;
        color: white;
    }

    .block-container {
        padding: 2rem;
        background-color: rgba(11, 15, 26, 0.85);
        border-radius: 16px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.6);
    }

    .dashboard-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 30px;
        padding: 30px 10px;
    }

    .card {
        background-color: #000000cc;
        border: 3px solid white;
        border-radius: 25px;
        padding: 30px;
        text-align: center;
        box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.8);
    }

    .card h3 {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 15px;
        color: white;
    }

    .card p {
        font-size: 28px;
        font-weight: bold;
        color: #00FF00;
        margin: 0;
    }

    .card .icon {
        font-size: 48px;
        color: #00FF00;
    }
    </style>
""", unsafe_allow_html=True)

# Conteúdo centralizado
st.markdown("<div class='dashboard-grid'>", unsafe_allow_html=True)

# Bloco 1 – Lucro Bruto
st.markdown("""
    <div class='card'>
        <h3>LUCRO BRUTO</h3>
        <p>R$ 15.800,00</p>
    </div>
""", unsafe_allow_html=True)

# Bloco 2 – Viagens Este Mês
st.markdown("""
    <div class='card'>
        <h3>VIAGENS ESTE MÊS</h3>
        <p>12</p>
    </div>
""", unsafe_allow_html=True)

# Bloco 3 – Lucro Líquido
st.markdown("""
    <div class='card'>
        <h3>LUCRO LÍQUIDO</h3>
        <p>R$ 10.320,00</p>
    </div>
""", unsafe_allow_html=True)

# Bloco 4 – Gráfico de crescimento (ícone)
st.markdown("""
    <div class='card'>
        <h3>&nbsp;</h3>
        <div class='icon'>📈</div>
    </div>
""", unsafe_allow_html=True)

# Fim da grade
st.markdown("</div>", unsafe_allow_html=True)
