import streamlit as st
import pandas as pd
import plotly.express as px

import os

# Obtener la ruta correcta dentro del proyecto en Render
file_path = os.path.join(os.getcwd(), "fastfood_data.csv")

# Cargar el archivo
fastfood_data = pd.read_csv(file_path)

# Headers

st.header("Fast food content data for different restaurants")


# Exploratory analisis

# Create a button that when clicking, builds a histogram

histogram_button = st.button("Show histogram")

if histogram_button:
    st.write("Histogram that shows count of observations by restaurant chain")
    histogram = px.histogram(fastfood_data, x="Company") # create histogram
    st.plotly_chart(histogram, use_container_width=True)

# Create a checkbox that when checked, builds a scatter plot
scatter_box = st.checkbox("Show scatter plot")

if scatter_box:
    st.write("Scatter plot for the data")
   
    scatter = px.scatter(fastfood_data, x="Item", y="Calories") # create scatter plot
    st.plotly_chart(scatter, use_container_width=True)



