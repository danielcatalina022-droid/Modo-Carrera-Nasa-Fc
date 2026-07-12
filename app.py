import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(page_title="NASA FC - Central de Operaciones", page_icon="🚀", layout="wide")

# Estilos CSS personalizados para simular Periódicos, WhatsApp y Twitter
st.markdown("""
<style>
    .diario-marca { border-top: 6px solid #e2001a; padding: 15px; background: #1a1a1a; border-radius: 4px; margin-bottom: 15px; }
    .diario-as { border-top: 6px solid #f9a800; padding: 15px; background: #1a1a1a; border-radius: 4px; margin-bottom: 15px; }
    .diario-mundo { border-top: 6px solid #0056a4; padding: 15px; background: #1a1a1a; border-radius: 4px; margin-bottom: 15px; }
    
    .burbuja-whatsapp { background-color: #0b141a; padding: 12px; border-radius: 10px; margin-bottom: 10px; max-width: 85%; border-left: 5px solid #25d366; }
    .tuit-romano { background-color: #15202b; padding: 15px; border-radius: 12px; margin-bottom: 15px; border: 1px solid #38444d; }
</style>
""", unsafe_allow_html=True)

st.title("🚀 NASA FC: Central de Prensa y Vestuario")
st.subheader("El Companion dinámico para el universo de tus Modos Carrera")

# Inicialización de bases de datos temporales
if 'noticias' not in st.session_state: st.session_state.noticias = []
if 'whatsapp' not in st.session_state: st.session_state.whatsapp = []
if 'tuits' not in st.session_state: st.session_state.tuits = []

# COLUMNA LATERAL: SUBIDA DE ARCHIVOS Y REGLAS
st.sidebar.header("📁 Datos del Modo Carrera")
archivo = st.sidebar.file_uploader("Sube pantallazos de tus partidos o juveniles", type=["png", "jpg", "jpeg"])
if archivo:
    st.sidebar.image(archivo, caption="📸 Captura del juego vinculada", use_container_width=True)

st.sidebar.divider()
club = st.sidebar.text_input("Nombre de tu Club Ficticio:", value="NASA FC")
presupuesto = st.sidebar.number_input("Presupuesto Actual (M€):", value=45)

# PANEL DE ACCIÓN: GENERADOR DE EVENTOS AUTOMÁTICOS
st.header("⏳ Avanzar Jornada en el Calendario")
col_ctrl, col_vacia = st.columns([2, 2])

with col_ctrl:
    rival = st.text_input("Próximo Rival en Liga:", value="Mostoles CF")
    if st.button("⚽ Jugar Partido y Generar Reacciones"):
        goles_pro = random.randint(0, 4)
        goles_contra = random.randint(0, 3)
        hora_actual = time.strftime("%H:%M")
        
        # Lógica de prensa española (Marca, As, Mundo Deportivo)
        diarios = [
            {"nombre": "Diario MARCA", "clase": "diario-marca"},
            {"nombre": "Diario AS", "clase": "diario-as"},
            {"nombre": "Mundo Deportivo", "clase": "diario-mundo"}
        ]
        diario_elegido = random.choice(diarios)
        
        if goles_pro > goles_contra:
            titular = f"¡Escándalo en el marcador! El {club} destroza tácticamente al {rival}."
            msg_segundo = "¡Enorme míster! Vaya tres puntos nos traemos. El vestuario está bailando, mañana entrenamos suave."
            tuit_text = f"🚨 EXCLUSIVA: Locura total con el rendimiento del {club}. Varios clubes de primera división empiezan a sondear la cláusula de su delantero estrella tras el recital ante el {rival}. Here we go! ⏳"
        elif goles_pro == goles_contra:
            titular = f"Tablas insuficientes. El {club} no logra romper el muro del {rival}."
            msg_segundo = "Míster, nos faltó colgar balones al final. Hay que ajustar la estrategia a balón parado esta semana."
            tuit_text = f"🔎 INFORMACIÓN: Empate amargo para el {club}. Las negociaciones por la renovación de su pivote defensivo se congelan tras el partido de hoy. Exigen subida salarial."
        else:
            titular = f"🚨 Debacle absoluta. El {rival} saca los colores a la defensa del {club}."
            msg_segundo = "Jefe, la directiva está pidiendo explicaciones por el cambio táctico del minuto 70. Los ánimos están tensos."
            tuit_text = f"⚠️ ALERTA: Crisis interna en el {club}. Kolderiu tendría que tomar decisiones drásticas en el próximo mercado invernal si quiere salvar los objetivos del año."

        # Guardar en los históricos de la sesión
        st.session_state.noticias.insert(0, {"diario": diario_elegido["nombre"], "clase": diario_elegido["clase"], "titular": titular, "hora": hora_actual})
        st.session_state.whatsapp.insert(0, {"msg": msg_segundo, "hora": hora_actual})
        st.session_state.tuits.insert(0, {"texto": tuit_text, "hora": hora_actual})

st.divider()

# DISTRIBUCIÓN DE LAS TRES PANTALLAS EN PARALELO
col_prensa, col_chat, col_twitter = st.columns(3)

with col_prensa:
    st.subheader("📰 Kiosco de Prensa")
    if st.session_state.noticias:
        for n in st.session_state.noticias[:2]:
            st.markdown(f"""
            <div class="{n['clase']}">
                <span style="font-weight: bold; color: #fff; font-size: 0.9em;">{n['diario']}</span>
                <span style="float: right; color: #888; font-size: 0.8em;">⏱️ {n['hora']}</span>
                <h3 style="margin-top: 8px; font-family: 'Georgia', serif; color: #fff; line-height: 1.2;">{n['titular']}</h3>
                <p style="color: #aaa; font-size: 0.85em; margin-bottom: 0;">Análisis de nuestros enviados especiales al estadio.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.caption("Esperando el pitido final para lanzar las portadas...")

with col_chat:
    st.subheader("💬 WhatsApp: Segundo Entrenador")
    if st.session_state.whatsapp:
        for w in st.session_state.whatsapp[:2]:
            st.markdown(f"""
            <div class="burbuja-whatsapp">
                <strong style="color: #25d366; font-size: 0.9em;">Segundo Entrenador 📋</strong>
                <p style="margin: 5px 0; color: #e9edef; font-size: 0.95em;">{w['msg']}</p>
                <span style="color: #8696a0; font-size: 0.75em; float: right;">{w['hora']} ✅✅</span>
                <div style="clear: both;"></div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.caption("Sin mensajes pendientes en el vestuario.")

with col_twitter:
    st.subheader("🐦 Mercado de Fichajes en X")
    if st.session_state.tuits:
        for t in st.session_state.tuits[:2]:
            st.markdown(f"""
            <div class="tuit-romano">
                <strong style="color: #1d9bf0;">Fabrizio Romano ✔️</strong> <span style="color: #6e767d; font-size: 0.85em;">@FabrizioRomano · {t['hora']}</span>
                <p style="margin-top: 8px; color: #e7e9ea; font-size: 0.95em; font-family: sans-serif;">{t['texto']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.caption("El mercado de rumores está tranquilo por ahora.")
