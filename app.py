import streamlit as st
import pandas as pd
import plotly.express as px
import numpy

# Read the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('vehicles_us.csv')
    return data

data = load_data()

## Preprocessing the data
# Handling missing values in 'is_4wd'
data['is_4wd'] = data['is_4wd'].fillna(0).astype(bool)

# Handling missing values in 'paint_color'
data['paint_color'] = data['paint_color'].fillna('unknown')

# Checking the relationship between 'model_year', 'cylinders', 'odometer' and other features
# to determine the best way to fill their missing values
model_year_rel = data[['model_year', 'model', 'type']].groupby(['model', 'type']).median()
cylinders_rel = data[['cylinders', 'model', 'type']].groupby(['model', 'type']).median()
odometer_rel = data[['odometer', 'model', 'type']].groupby(['model', 'type']).median()

# Fill 'model_year'
data['model_year'] = data.groupby(['model', 'type'])['model_year'].transform(lambda x: x.fillna(x.median()))

# Fill 'cylinders'
data['cylinders'] = data.groupby(['model', 'type'])['cylinders'].transform(lambda x: x.fillna(x.median()))

# Fill 'odometer'
data['odometer'] = data.groupby(['model', 'type'])['odometer'].transform(lambda x: x.fillna(x.median()))

# Streamlit app layout
st.title('Vehicle Data Analysis')

# Display the first few rows of the dataframe
st.subheader('Data Overview')
st.write(data.head())

# Checkboxes for showing different plots
if st.checkbox('Show Histogram of Vehicle Prices'):
    histogram = px.histogram(data, x='price', nbins=50, title='Histogram of Vehicle Prices')
    st.plotly_chart(histogram)

if st.checkbox('Show Scatterplot of Odometer vs Price'):
    scatterplot = px.scatter(data, x='odometer', y='price', title='Scatterplot of Odometer vs Price')
    st.plotly_chart(scatterplot)

if st.checkbox('Show Histogram of Vehicle Model Years'):
    model_year_histogram = px.histogram(data, x='model_year', nbins=50, title='Histogram of Vehicle Model Years')
    st.plotly_chart(model_year_histogram)

if st.checkbox('Show Scatterplot of Days Listed vs Price'):
    days_price_scatterplot = px.scatter(data, x='days_listed', y='price', title='Scatterplot of Days Listed vs Price')
    st.plotly_chart(days_price_scatterplot)


# Streamlit interface
# def main():
#     st.title("Vehicle Data Exploration App")
#
#     # Header
#     st.header("Exploratory Data Analysis of Vehicle Dataset")
#
#     # Histogram
#     st.subheader("Histogram of Vehicle Prices")
#     hist_values = st.slider('Select the number of bins for the histogram:', 10, 100, 50)
#     fig_hist = px.histogram(data, x='price', nbins=hist_values)
#     st.plotly_chart(fig_hist)
#
#     # Scatter Plot
#     st.subheader("Scatter Plot of Odometer vs Price")
#     scatter_log_scale = st.checkbox('Use Log Scale for Price', value=False)
#     if scatter_log_scale:
#         fig_scatter = px.scatter(data, x='odometer', y='price', log_y=True)
#     else:
#         fig_scatter = px.scatter(data, x='odometer', y='price')
#     st.plotly_chart(fig_scatter)
#
# if __name__ == "__main__":
#     main()
