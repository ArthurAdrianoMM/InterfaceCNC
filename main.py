import streamlit as st
import requests
import time

st.set_page_config(layout="wide")

API_URL = "https://interfacecnc-api.onrender.com/cnc-data" 
refresh_interval = 5  # segundos

#st.title("Monitoramento CNC - Dashboard")

# puxa dados
def get_data():
    try:
        response = requests.get(API_URL, timeout=5)
        return response.json()
    except:
        return None

# estilo
st.markdown("""
    <style>
        .card {
            background-color: #111;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            color: #0f0;
            font-family: sans-serif;
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
            margin-bottom: 20px;
        }
        .label {
            font-size: 20px;
            color: #888;
        }
        .value {
            font-size: 36px;
            font-weight: bold;
        }
        .element-container {
            padding-right: 15px !important;
            padding-left: 15px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Atualuzacao
placeholder = st.empty()

while True:
    data = get_data()

    if data:
        with placeholder.container():
            col1, col2, col3, col4 = st.columns([1, 1, 1, 1], gap="large")
            col5, col6, col7, col8 = st.columns([1, 1, 1, 1], gap="large")
            col9, col10 = st.columns([1, 1], gap="large")

            with col1:
                st.markdown(f"""<div class='card'><div class='label'>Avanço</div><div class='value'>{data['avanco']} mm/min</div></div>""", unsafe_allow_html=True)
            with col2:
                st.markdown(f"""<div class='card'><div class='label'>RPM</div><div class='value'>{data['rpm']} rpm</div></div>""", unsafe_allow_html=True)
            with col3:
                st.markdown(f"""<div class='card'><div class='label'>Profundidade</div><div class='value'>{data['profundidade']} mm</div></div>""", unsafe_allow_html=True)
            with col4:
                st.markdown(f"""<div class='card'><div class='label'>MTTR</div><div class='value'>{data['mttr']} h</div></div>""", unsafe_allow_html=True)

            with col5:
                st.markdown(f"""<div class='card'><div class='label'>MTTF</div><div class='value'>{data['mttf']} h</div></div>""", unsafe_allow_html=True)
            with col6:
                st.markdown(f"""<div class='card'><div class='label'>FF</div><div class='value'>{data['ff']}</div></div>""", unsafe_allow_html=True)
            with col7:
                st.markdown(f"""<div class='card'><div class='label'>Corrente Motor</div><div class='value'>{data['corrente_motor']} A</div></div>""", unsafe_allow_html=True)
            with col8:
                st.markdown(f"""<div class='card'><div class='label'>Tensão Motor</div><div class='value'>{data['tensao_motor']} V</div></div>""", unsafe_allow_html=True)

            with col9:
                st.markdown(f"""<div class='card'><div class='label'>Vibração Fuso</div><div class='value'>{data['vibracao_fuso']} mm/s</div></div>""", unsafe_allow_html=True)
            with col10:
                st.markdown(f"""<div class='card'><div class='label'>Vibração Ferramenta</div><div class='value'>{data['vibracao_ferramenta']} mm/s</div></div>""", unsafe_allow_html=True)

    else:
        placeholder.error("Erro ao acessar a API")

time.sleep(refresh_interval) 

