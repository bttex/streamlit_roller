import streamlit as st
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import writers
import io
import numpy as np
import tempfile  # Importa tempfile
import os

# Configurações do PWA
st.set_page_config(page_title="Rolador de Dados", layout="centered",page_icon=':game_die:')

st.markdown(
    """
    <link rel="manifest" href="manifest.json">
    <script>
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('service-worker.js')
            .then(function(registration) {
                console.log('ServiceWorker registrado com sucesso:', registration.scope);
            }).catch(function(error) {
                console.log('Falha ao registrar ServiceWorker:', error);
            });
        }
    </script>
    """,
    unsafe_allow_html=True,
)

def rolar_dado(num_lados):
    return random.randint(1, num_lados)

# Inicializa o histórico de rolagens na sessão do Streamlit
if 'historico_rolagens' not in st.session_state:
    st.session_state.historico_rolagens = []

# Interface do Streamlit
st.title("Rolador de Dados de D&D")
tipo_dado = st.selectbox("Selecione o tipo de dado", options=[4, 6, 8, 10, 12, 20, 100], index=5)
quantidade = st.number_input("Quantos dados deseja rolar?", min_value=1, max_value=10, value=1, step=1)
modificador = st.number_input("Modificador (+/-):", step=1, value=0)

if st.button("Rolar Dados"):
    with st.spinner("Calculando..."):
        resultados = [rolar_dado(tipo_dado) for _ in range(quantidade)]
        resultado_com_modificador = sum(resultados) + modificador

        # Adiciona a rolagem ao histórico
        st.session_state.historico_rolagens.insert(0, f"{quantidade}d{tipo_dado} + {modificador} = {resultado_com_modificador} ({resultados})")

        # Mantém apenas as últimas 5 rolagens no histórico
        if len(st.session_state.historico_rolagens) > 5:
            st.session_state.historico_rolagens.pop()

        st.success(f"Resultados: {resultados} (Modificador: {modificador})")
        st.success(f"Resultado final com modificador: {resultado_com_modificador}")

    # Exibe o histórico de rolagens
    st.subheader("Histórico de Rolagens:")
    for rolagem in st.session_state.historico_rolagens:
        st.write(rolagem)