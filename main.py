import streamlit as st
import requests
import time

API_URL = "https://interfacecnc-api.onrender.com/cnc-data"  

st.set_page_config(page_title="Monitoramento CNC", layout="centered")
st.title("🛠️ Monitoramento CNC em Tempo Real")

placeholder = st.empty()
refresh_interval = 5  # segundos

while True:
    try:
        r = requests.get(API_URL)
        data = r.json()
    except Exception as e:
        placeholder.error(f"Erro na API: {e}")
        time.sleep(refresh_interval)
        continue

    with placeholder.container():
        st.subheader("📌 Parâmetros Operacionais")
        st.metric("Avanço", f"{data['avanco']} mm/min")
        st.metric("RPM", f"{data['rpm']} rpm")
        st.metric("Profundidade de Corte", f"{data['profundidade']} mm")

        st.subheader("⚙️ Indicadores de Manutenção")
        st.metric("MTTR", f"{data['mttr']} h")
        st.metric("MTTF", f"{data['mttf']} h")
        st.metric("Fator de Falha (FF)", f"{data['ff']}")

        st.subheader("🔌 Motor")
        st.metric("Corrente", f"{data['corrente_motor']} A")
        st.metric("Tensão", f"{data['tensao_motor']} V")

        st.subheader("🌀 Vibração")
        st.metric("Fuso", f"{data['vibracao_fuso']} mm/s")
        st.metric("Ferramenta", f"{data['vibracao_ferramenta']} mm/s")

    time.sleep(refresh_interval)
