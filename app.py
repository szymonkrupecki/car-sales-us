import streamlit as st
import pandas as pd
import plotly.express as px
import numpy

# Read the dataset
@st.cache  # This decorator caches the data to speed up the app
def load_data():
    data = pd.read_csv('vehicles_us.csv')
    return data

data = load_data()

# Streamlit interface
def main():
    st.title("Vehicle Data Exploration App")

    # Header
    st.header("Exploratory Data Analysis of Vehicle Dataset")

    # Histogram
    st.subheader("Histogram of Vehicle Prices")
    hist_values = st.slider('Select the number of bins for the histogram:', 10, 100, 50)
    fig_hist = px.histogram(data, x='price', nbins=hist_values)
    st.plotly_chart(fig_hist)

    # Scatter Plot
    st.subheader("Scatter Plot of Odometer vs Price")
    scatter_log_scale = st.checkbox('Use Log Scale for Price', value=False)
    if scatter_log_scale:
        fig_scatter = px.scatter(data, x='odometer', y='price', log_y=True)
    else:
        fig_scatter = px.scatter(data, x='odometer', y='price')
    st.plotly_chart(fig_scatter)

if __name__ == "__main__":
    main()
