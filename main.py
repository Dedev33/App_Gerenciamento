import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Painel de Transporte",
    page_icon="🧾",
    layout="wide"
)

# CSS baseado na imagem enviada
st.markdown("""
    <style>
    html, body, [class*="css"] {
        background: url('https://raw.githubusercontent.com/Dedev33/App_Gerenciamento/main/banner.jpg.jpeg') no-repeat center center fixed;
        background-size: cover;
        font-family: 'Segoe UI', sans-serif;
        color: white;
    }

    .overlay {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 50px 0;
        border-radius: 0;
    }

    .dashboard {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 40px;
        max-width: 900px;
        margin: 0 auto;
    }

    .card {
        background-color: #000000cc;
        border-radius: 40px;
        border: 3px solid white;
        padding: 40px;
        text-align: center;
        box-shadow: 0px 8px 16px rgba(0,0,0,0.8);
    }

    .card h3 {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
        color: white;
    }

    .card p {
        font-size: 28px;
        font-weight: bold;
        color: #00FF00;
        margin: 0;
    }

    .icon {
        font-size: 50px;
        color: #00FF00;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Conteúdo com filtro escuro no fundo
st.markdown("<div class='overlay'>", unsafe_allow_html=True)
st.markdown("<div class='dashboard'>", unsafe_allow_html=True)

# Card 1 – Lucro Bruto
st.markdown("""
    <div class='card'>
        <h3>LUCRO BRUTO</h3>
        <p>R$ 15.800,00</p>
    </div>
""", unsafe_allow_html=True)

# Card 2 – Viagens Este Mês
st.markdown("""
    <div class='card'>
        <h3>VIAGENS ESTE MÊS</h3>
        <p>12</p>
    </div>
""", unsafe_allow_html=True)

# Card 3 – Lucro Líquido
st.markdown("""
    <div class='card'>
        <h3>LUCRO LÍQUIDO</h3>
        <p>R$ 10.320,00</p>
    </div>
""", unsafe_allow_html=True)

# Card 4 – Gráfico
st.markdown("""
    <div class='card'>
        <h3>&nbsp;</h3>
        <div class='icon'>📈</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
