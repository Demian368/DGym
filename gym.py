import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Asistente Pro de Gimnasio", layout="wide")

# Inicialización de estado global
if "log" not in st.session_state:
    st.session_state.log = []
if "step_37" not in st.session_state:
    st.session_state.step_37 = 0  # 0: reposo, 1-5: series activas, 6: descanso largo, 7: completado
if "series_37_count" not in st.session_state:
    st.session_state.series_37_count = 0

# Título principal
st.title("💪 Asistente Pro de Gimnasio")
st.markdown("---")

# Menú lateral
menu = ["Registro de Cargas", "Rutinas y Modalidades", "Método 3/7"]
seleccion = st.sidebar.selectbox("Navegación", menu)

# --- MÓDULO 1: REGISTRO DE CARGAS ---
if seleccion == "Registro de Cargas":
    st.header("📊 Registro y Seguimiento de Cargas")
    
    col1, col2 = st.columns(2)
    with col1:
        ejercicio = st.text_input("Nombre del Ejercicio", placeholder="Ej. Press de Banca")
        peso = st.number_input("Peso (kg)", min_value=0.5, step=0.5)
    with col2:
        series = st.number_input("Series", min_value=1, step=1, value=3)
        reps = st.number_input("Repeticiones", min_value=1, step=1, value=10)
    
    if st.button("Guardar Serie", type="primary"):
        if ejercicio:
            st.session_state.log.append({
                "Tipo": "Estándar",
                "Ejercicio": ejercicio, 
                "Peso (kg)": peso, 
                "Series": series, 
                "Reps": reps
            })
            st.success("¡Registro guardado con éxito!")
        else:
            st.warning("Por favor, ingresa el nombre del ejercicio.")
            
    if st.button("Limpiar Historial General", type="secondary"):
        st.session_state.log = []
        st.session_state.series_37_count = 0
        st.rerun()
    
    st.markdown("### Historial de Entrenamiento")
    if st.session_state.log:
        st.table(st.session_state.log)
    else:
        st.info("No hay registros aún. ¡Completa tu primer ejercicio!")

# --- MÓDULO 2: RUTINAS Y MODALIDADES ---
elif seleccion == "Rutinas y Modalidades":
    st.header("📋 Modalidades de Entrenamiento y Recomendaciones")
    
    modo = st.selectbox(
        "Selecciona tu enfoque",
        ["PPL (Push/Pull/Legs)", "Full Body", "Arnold Split", "Calistenia"]
    )
    
    st.markdown("---")
    
    if modo == "PPL (Push/Pull/Legs)":
        st.subheader("Estructura: Empuje / Tracción / Pierna")
        st.write("Ideal para frecuencias de 3 a 6 días por semana, separando patrones de movimiento.")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.info("**Día 1: Empuje (Pecho/Hombro/Tríceps)**\n* Press Militar\n* Aperturas con mancuernas\n* Extensiones de tríceps")
        with c2:
            st.info("**Día 2: Tracción (Espalda/Bíceps)**\n* Dominadas o Jalón al pecho\n* Remo con barra\n* Curl de bíceps")
        with c3:
            st.info("**Día 3: Pierna (Cuádriceps/Isios/Gemelo)**\n* Sentadilla con barra\n* Peso muerto rumano\n* Elevación de talones")
            
    elif modo == "Full Body":
        st.subheader("Estructura: Cuerpo Completo")
        st.write("Alta frecuencia para estimular todos los grupos musculares en cada sesión.")
        st.warning("Recomendación: Deja un día de descanso entre sesiones.")
        st.write("• **Bloque Principal:** Sentadillas, Press de Banca, Remo Pendlay.\n• **Accesorios:** Zancadas y Planchas abdominales.")

    elif modo == "Arnold Split":
        st.subheader("Estructura: Variante Clásica de Arnold Schwarzenegger")
        st.write("Combina grupos musculares antagonistas para maximizar el bombeo y densidad muscular.")
        with st.expander("Ver distribución de días"):
            st.write("**Día A (Pecho y Espalda):** Superseries de press y remos.\n**Día B (Hombros y Brazos):** Enfoque en deltoides y brazos grandes.\n**Día C (Pierna completa):** Énfasis en sentadilla y prensa.")

    elif modo == "Calistenia":
        st.subheader("🏋️‍♂️ Bloque de Calistenia Pura")
        st.write("Entrenamiento con peso corporal. Adapta la dificultad según tu nivel.")
        
        ej_cal = st.selectbox("Elige un ejercicio para ver progresiones", ["Flexiones", "Dominadas", "Fondos"])
        
        col_p1, col_p2 = st.columns(2)
        if ej_cal == "Flexiones":
            col_p1.success("🟢 Principiante: Con rodillas apoyadas o manos en pared.")
            col_p2.error("🔴 Avanzado: Flexiones diamante o a una mano.")
        elif ej_cal == "Dominadas":
            col_p1.success("🟢 Principiante: Dominadas negativas o con banda elástica.")
            col_p2.error("🔴 Avanzado: Dominadas explosivas al pecho o con lastre.")
        elif ej_cal == "Fondos":
            col_p1.success("🟢 Principiante: Fondos en banco.")
            col_p2.error("🔴 Avanzado: Fondos en paralelas lastrados.")

# --- MÓDULO 3: MÉTODO 3/7 ---
elif seleccion == "Método 3/7":
    st.header("⏱️ Entrenador del Método 3/7")
    st.write("Realiza 5 series progresivas (3, 4, 5, 6, 7 reps). Descansos cortos de 15s, y 2.5 min al finalizar.")
    
    # Panel de configuración del bloque
    with st.expander("Configuración del Ejercicio Actual", expanded=True):
        ej_37 = st.text_input("Ejercicio para el Método 3/7", placeholder="Ej. Curl de Bíceps")
        peso_37 = st.number_input("Peso utilizado (kg)", min_value=0.5, step=0.5, value=10.0)
    
    st.metric(label="Series Completadas de 3/7", value=st.session_state.series_37_count)
    
    repeticiones_37 = [3, 4, 5, 6, 7]
    
    if st.session_state.step_37 == 0:
        st.info("El método busca la máxima congestión muscular mediante fatiga acumulada.")
        if st.button("Iniciar Nuevo Bloque 3/7", type="primary"):
            if ej_37:
                st.session_state.step_37 = 1
                st.rerun()
            else:
                st.warning("Por favor, ingresa el nombre del ejercicio antes de iniciar.")
            
    elif 1 <= st.session_state.step_37 <= 4:
        serie_actual = st.session_state.step_37
        reps_objetivo = repeticiones_37[serie_actual - 1]
        
        st.subheader(f"Fase {serie_actual}/5")
        st.metric(label="Objetivo de Repeticiones", value=f"{reps_objetivo} reps")
        
        if st.button(f"Completé las {reps_objetivo} reps - Descanso Corto (15s)", type="secondary"):
            with st.spinner("Contando 15 segundos de descanso..."):
                barra = st.progress(0)
                for i in range(15):
                    time.sleep(1)
                    barra.progress((i + 1) / 15)
            
            st.session_state.step_37 += 1
            st.rerun()

    elif st.session_state.step_37 == 5:
        # Fase final: 7 repeticiones
        reps_objetivo = repeticiones_37[4]
        st.subheader("🔥 Fase Final: 5/5 (7 Repeticiones)")
        st.metric(label="Objetivo", value=f"{reps_objetivo} reps")
        
        if st.button(f"¡Completé las últimas {reps_objetivo} reps! - Descanso Largo", type="primary"):
            st.session_state.step_37 = 6
            st.rerun()
            
    elif st.session_state.step_37 == 6:
        st.subheader("🎉 ¡Serie de 3/7 completada!")
        st.warning("Iniciando descanso largo de recuperación (2 minutos y 30 segundos).")
        
        with st.spinner("Recuperando energías (150 segundos)..."):
            barra_larga = st.progress(0)
            tiempo_total = 150  # 2.5 minutos
            for i in range(tiempo_total):
                time.sleep(1)
                barra_larga.progress((i + 1) / tiempo_total)
        
        # Registro automático del bloque completado
        st.session_state.series_37_count += 1
        st.session_state.log.append({
            "Tipo": "Método 3/7",
            "Ejercicio": ej_37,
            "Peso (kg)": peso_37,
            "Series": "Ciclo 3/7",
            "Reps": "3-4-5-6-7"
        })
        
        st.session_state.step_37 = 7
        st.rerun()
        
    elif st.session_state.step_37 == 7:
        st.balloons()
        st.success("¡Bloque completo del Método 3/7 terminado y registrado con éxito!")
        if st.button("Reiniciar Entrenador", type="secondary"):
            st.session_state.step_37 = 0
            st.rerun()