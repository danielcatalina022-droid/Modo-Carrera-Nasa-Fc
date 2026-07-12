import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Creador de Modos Carrera", page_icon="🎮", layout="wide")
st.title("🎮 Creador de Modos Carrera Personalizados")
st.subheader("Diseña tu club, establece tus reglas de fichaje y simula tu temporada")

if 'modo_carrera_creado' not in st.session_state:
    st.session_state.modo_carrera_creado = False
if 'historial_partidos' not in st.session_state:
    st.session_state.historial_partidos = []

if not st.session_state.modo_carrera_creado:
    st.header("🚀 Paso 1: Configura tu Club")
    with st.form("config_form"):
        col1, col2 = st.columns(2)
        with col1:
            nombre_club = st.text_input("Nombre de tu Club:", placeholder="Ej. NASA FC...")
            presupuesto = st.number_input("Presupuesto Inicial (M€):", min_value=1, max_value=1000, value=50)
            objetivo = st.selectbox("Objetivo:", ["Evitar el descenso", "Mitad de tabla", "Ascenso Directo", "Ganar la Liga"])
        with col2:
            st.write("🔒 **Reglas Especiales:**")
            regla_cantera = st.checkbox("Solo jugadores de la cantera")
            regla_edad = st.checkbox("Prohibido fichar mayores de 23 años")
            regla_clausulas = st.checkbox("Cláusulas de rescisión obligatorias")
        submit = st.form_submit_button("💥 Inicializar Modo Carrera")
        if submit and nombre_club:
            st.session_state.club = nombre_club
            st.session_state.presupuesto = presupuesto
            st.session_state.objetivo = objetivo
            st.session_state.reglas = {"Cantera": regla_cantera, "Edad": regla_edad, "Cláusulas": regla_clausulas}
            st.session_state.plantilla = [
                {"Jugador": "Capitán Original", "Posición": "MC", "Media": 75, "Edad": 24},
                {"Jugador": "Promesa Local", "Posición": "DC", "Media": 68, "Edad": 18}
            ]
            st.session_state.modo_carrera_creado = True
            st.rerun()
else:
    st.header(f"⚽ Panel de Control: {st.session_state.club}")
    st.write(f"Presupuesto: {st.session_state.presupuesto} M€ | Objetivo: {st.session_state.objetivo}")
    
    tab1, tab2 = st.tabs(["📋 Plantilla", "⚔️ Simular Partido"])
    with tab1:
        st.dataframe(pd.DataFrame(st.session_state.plantilla), use_container_width=True)
    with tab2:
        rival = st.text_input("Rival:", value="Rival FC")
        if st.button("🎯 Simular Partido"):
            goles_pro = random.randint(0, 4)
            goles_contra = random.randint(0, 3)
            res = f"{st.session_state.club} {goles_pro} - {goles_contra} {rival}"
            st.success(res) if goles_pro > goles_contra else st.error(res)
