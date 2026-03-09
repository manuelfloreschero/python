import streamlit as st
import carga_datos
import informacion
import analisis

# Configuración de la aplicación
st.set_page_config(page_title="Mi Aplicación", layout="wide")

# Sidebar para navegación
st.sidebar.title("Navegación")
opcion = st.sidebar.selectbox(
    "Selecciona un módulo:",
    ("Home", "Módulo 1", "Módulo 2", "Módulo 3", "Módulo 4")
)

# Contenido según la opción seleccionada
if opcion == "Home":
    st.header("**PROYECTO:** Análisis Exploratorio de Datos de un Banco")
    st.write("""
    - El objetivo del proyecto es realizar un análisis exploratorio de datos, para la toma de decisiones.
    """)

    st.write("**Nombre de Alumno:** Flores Chero Luiguin Manuel")
    st.write("**Curso:** Especialización en Python for Analytics")
    st.write("**Año:** 2026")
    st.write("""**Descripción del Data Set:** El data set cuenta con información principal de:
    """)
    st.write("""
    - Clientes de una empresa de telecomunicaciones, donde podemos encontrar información de contratos y pagos realizados.
    """)
    
    st.write("**Tecnologías:** Para este proyecto se han utilizado. ")
    st.write("""
    - **Python**: Lenguaje de programación principal.
    - **Streamlit**: Para la interfaz gráfica interactiva.
    - **Pandas**: Manipulación y análisis de datos estructurados.
    - **Numpy**: Manejo de arreglos multidimensionales.
    """)
    st.info("Usa el menú lateral para moverte entre módulos.")

elif opcion == "Módulo 1":
    st.title("Módulo 1 - Carga de Dataset")
    st.write("Aquí puedes cargar y procesar tus datos.")
    carga_datos.cargar_datos()

elif opcion == "Módulo 2":
    st.title("Módulo 2 - Carga de Dataset")
    st.write("Aquí puedes cargar y procesar tus datos.")
    if 'df' in st.session_state:  # Usar el dataset cargado previamente
        info = informacion.InfoDataset(st.session_state['df'])
        info.mostrar_info()
    else:
        st.warning("Primero carga tus datos en el módulo de Carga de Datos.")


elif opcion == "Módulo 3":
    st.title("Módulo 3 - Analisis")
    st.write("Aquí puedes visualizar Estadisticas Descriptivas")
    if 'df' in st.session_state:
        analisis_dataset = analisis.AnalisisDataset(st.session_state['df'])
        analisis_dataset.mostrar_estadisticas()
    else:
        st.warning("Primero carga tus datos en el módulo de Carga de Datos.")



elif opcion == "Módulo 4":
    st.title("Módulo 4 - Reportes automáticos")
    st.write("Aquí puedes generar reportes en PDF o Excel.")