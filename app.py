import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar dataset
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Análisis de anuncios de coches en USA")

# Botón para histograma
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Creación de un gráfico de dispersión: precio vs odómetro')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
