import streamlit as st
import time

st.title("Asistente de Gimnasio Avanzado")

# Inicializar estado para el registro y el método 3/7
if "log" not in st.session_state:
    st.session_state.log = []
if "step_37" not in st.session_state:
    st.session_state.step_37 = 0  # 0: reposo, 1-5: serie activa

repeticiones_37 = [3, 4, 5, 6, 7]

menu = {"Registrar Ejercicio": 1, "Método 3/7": 2}
eleccion = st.sidebar.selectbox("Módulo", list(menu.keys()))

if menu[eleccion] == 1:
    st.header("Registro de Cargas")
    ejercicio = st.text_input("Nombre del ejercicio")
    peso = st.number_input("Peso (kg)", min_value=0.5, step=0.5)
    series = st.number_input("Series", min_value=1, step=1)
    reps = st.number_input("Repeticiones", min_value=1, step=1)
    
    if st.button("Guardar Serie"):
        st.session_state.log.append({"Ejercicio": ejercicio, "Peso": peso, "Series": series, "Reps": reps})
        st.success("¡Serie registrada!")
    
    if st.session_state.log:
        st.subheader("Tu Historial")
        st.table(st.session_state.log)

elif menu[eleccion] == 2:
    st.header("Entrenamiento Método 3/7")
    
    if st.session_state.step_37 == 0:
        if st.button("Iniciar Serie (3 reps)"):
            st.session_state.step_37 = 1
            st.rerun()
    else:
        serie_actual = st.session_state.step_37
        reps_objetivo = repeticiones_37[serie_actual - 1]
        st.subheader(f"Serie {serie_actual}/5 - Haz {reps_objetivo} repeticiones")
        
        if serie_actual < 5:
            if st.button("Terminé mis reps - Iniciar Descanso"):
                barra_progreso = st.progress(0)
                for i in range(15):
                    time.sleep(1)
                    progreso = (i + 1) / 15
                    barra_progreso.progress(progreso)
                st.session_state.step_37 += 1
                st.rerun()
        else:
            st.balloons()
            st.success("¡Bloque 3/7 completado con éxito!")
            if st.button("Reiniciar Método"):
                st.session_state.step_37 = 0
                st.rerun()