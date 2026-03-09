# analisis.py
import streamlit as st
import pandas as pd

class AnalisisDataset:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def mostrar_estadisticas(self):
        st.title("📊 Estadísticas Descriptivas del Dataset")

        # Crear pestañas
        tab1, tab2 = st.tabs(["Estadísticas numéricas", "Estadísticas categóricas"])

        # Estadísticas para variables numéricas
        with tab1:
            st.subheader("Variables numéricas")
            desc_num = self.df.describe(include=['int64', 'float64'])
            styled_num = desc_num.style.format("{:.2f}").highlight_max(color="lightgreen", axis=0)
            st.dataframe(styled_num, use_container_width=True)

        # Estadísticas para variables categóricas
        with tab2:
            st.subheader("Variables categóricas")
            desc_cat = self.df.describe(include=['object'])

            # Solo resaltar la columna 'freq' (numérica)
            if "freq" in desc_cat.columns:
                styled_cat = desc_cat.style.highlight_max(subset=["freq"], color="lightblue", axis=0)
            else:
                styled_cat = desc_cat.style

            st.dataframe(styled_cat, use_container_width=True)