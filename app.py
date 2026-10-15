import pandas as pd
import streamlit as st
import os
import matplotlib.pyplot as plt


df = pd.read_excel(r"YARDAS_PASOS_DATOS_TICS.xlsx", index_col=0)
st.dataframe(df.head())

st.header("estadistica descriptiva")
st.dataframe(df.describe())

df.columns= [c.lower().replace('', '_')for c in df.columns]

fig, ax = plt.subplot()
ax.boxplot(df['pases_completos'])
st.header("diagrama de caja y bigote\n de pases completos")
st.pyplot(fig)

fig, ax = plt.subplot()
ax.boxplot(df['yardas_totales'])
st.header("diagrama de caja bigote\n de yardas totales")
st.pyplot(fig)
