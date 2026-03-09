# modulo_info.py
import streamlit as st
import pandas as pd

class InfoDataset:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def mostrar_info(self):
        st.title("ℹ️ Información del Dataset")

        # Crear pestañas
        tab1, tab2, tab3, tab4 = st.tabs([
            "Información general", 
            "Tipos de datos", 
            "Valores nulos", 
            "Clasificación de variables"
        ])

        # Primer tab: información general
        with tab1:
            st.subheader("Información general del dataset")
            info_table = pd.DataFrame({
                "Filas": [self.df.shape[0]],
                "Columnas": [self.df.shape[1]],
                "Columnas únicas": [len(self.df.columns)],
                "Duplicados": [self.df.duplicated().sum()]
            })
            st.table(info_table)

        # Segundo tab: tipos de datos
        with tab2:
            st.subheader("Tipos de datos por columna")
            tipos = pd.DataFrame(self.df.dtypes, columns=["Tipo de dato"])
            st.dataframe(tipos)

        # Tercer tab: valores nulos
        with tab3:
            st.subheader("Conteo de valores nulos por columna")
            nulos = pd.DataFrame(self.df.isnull().sum(), columns=["Valores nulos"])
            st.dataframe(nulos)

        # Cuarto tab: clasificación de variables
        with tab4:
            st.subheader("Conteo de Tipo de variables")

            # Crear tabla con columnas y su tipo
            clasificacion = pd.DataFrame({
                "Columna": self.df.columns,
                "Tipo de variable": self.df.dtypes.replace({
                    "int64": "Numérica",
                    "float64": "Numérica",
                    "object": "Categórica"
                }).values
            })

            # Resumen de cuántas hay por tipo
            resumen = clasificacion["Tipo de variable"].value_counts().reset_index()
            resumen.columns = ["Tipo de variable", "Cantidad"]
            st.table(resumen)
            st.subheader("Lista de variables")
            st.dataframe(clasificacion)