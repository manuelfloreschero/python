# modulo_carga_datos.py
import streamlit as st
import pandas as pd

def cargar_datos():
    st.title("Carga de Datos")
    st.write("En este módulo se carga el dataset y se muestre información general del dataset")

    # Subida de archivo
    archivo = st.file_uploader("Sube tu archivo CSV", type=["csv"])

    if archivo is not None:
        try:
            # Intentar leer el archivo
            df = pd.read_csv(archivo)
            st.session_state['df'] = df


            # Confirmación de carga
            st.success("✅ El archivo fue cargado correctamente.")

            # Vista previa con head()
            st.subheader("Vista previa de los datos")
            st.dataframe(df.head())

            # Dimensiones del dataset
            filas, columnas = df.shape
            st.write(f"El dataset tiene **{filas} filas** y **{columnas} columnas**.")

        except Exception as e:
            st.error(f"❌ Error al cargar el archivo: {e}")
    else:
        st.info("Por favor, sube un archivo CSV para continuar.")