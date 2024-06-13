import streamlit as st
import pandas as pd
import numpy as np
import time
import country_converter as coco

import folium
import branca.colormap as cm
from streamlit_folium import folium_static
import plotly.express as px

st.title('Exploring Data')

st.markdown(
    """
    EDA:
    - Product who generates highest revenue & Lowest Revenue
    - Sales Trend
    - Country who generates hightst revenue

    """
)

df = pd.read_csv('dataset/cleaned_dataset_real.csv')

# @st.cache_data
# def show_data_EDA():
#     st.write(df)
# if st.checkbox('Show Data!'):
#     show_data_EDA()

#Product Revenue
# Aggregate the revenue & Quantity
prod_rev = df.groupby('ProductNo').agg({'ProductName': 'first', 'Revenue': 'sum',  'Quantity': 'sum'}).reset_index()
st.subheader('Product Revenue')
sort_order = st.selectbox('Select Sorting Order:', ['Highest to Lowest', 'Lowest to Highest'])
@st.cache_data()
def prod_revenue(sort_order):
    if sort_order == 'Highest to Lowest':
        sorted_revenue = prod_rev.sort_values(by='Revenue', ascending=False).head(10)
    else:
        sorted_revenue = prod_rev.sort_values(by='Revenue', ascending=True).head(10)

    fig = px.bar(sorted_revenue, x='Revenue', y='ProductName', color='Revenue',
                title=f'Top 10 Products by Revenue ({sort_order})',
                text_auto='.2s',
                labels={'ProductName': 'Product Name', 'Revenue': 'Total Revenue'})
    # fig.update_layout(yaxis={'categoryorder': 'total ascending' if sort_order == 'Highest to Lowest' else 'total descending'})
    fig.update_layout(
        yaxis={'categoryorder': 'total ascending' if sort_order == 'Highest to Lowest' else 'total descending'},
        margin=dict(l=200, r=20, t=50, b=50), # Adjust margins to prevent label cutoff
        yaxis_title=None,  
    )

    # Adjust the orientation of y-axis labels
    # fig.update_yaxes(tickangle=0, automargin=True)

    st.plotly_chart(fig, theme=None)
prod_revenue(sort_order)

# Sales Trend
# month
monthly_revenue = df.groupby('Month_Year')['Revenue'].sum()
# day
Day_Revenue = df.groupby('Day').agg({'Day_Name': 'first', 'Revenue': 'sum', 'TransactionNo': 'count'}).reset_index()
Day_Revenue = Day_Revenue.sort_values('Day', ascending = True)

st.subheader('Sales Trend Transaction')
@st.cache_data
def sales_trend():
    tab1, tab2 = st.tabs(["Sales Trend Over The Month", "Sales Trend Over The Day"])
    with tab1:
        fig = px.line(monthly_revenue, x = monthly_revenue.index, y = "Revenue", title = "Sales Trend Over the Month")
        fig.update_traces(mode = 'lines+markers')
        st.plotly_chart(fig, theme = 'streamlit')
    with tab2:
        fig = px.line(Day_Revenue, x = "Day_Name", y = "Revenue", title = "Sales Trend Over the Day")
        fig.update_traces(mode = 'lines+markers')
        st.plotly_chart(fig, theme="streamlit")
        st.markdown('Tuesday the store is close')

sales_trend()

st.subheader('Revenue by Country')
# Country
# Aggregating sales by countries
country_sales = df.groupby(by = 'CountryISO3', as_index = False)['Revenue'].sum()
# Adding the country name back (instead of just ISO3)
country_sales['Country'] = [coco.convert(i, to = 'name_short') for i in country_sales['CountryISO3']]
# revenue
Country_rev = country_sales.sort_values('Revenue', ascending=False).head(10)

@st.cache_data
def country():
    tab1, tab2 = st.tabs(["Top 10", "Revenue Distribution"])
    with tab1:
        fig = px.bar(Country_rev, x='Revenue', y='Country', color='Revenue', title='Top 10 Country with Highest Revenue')
        fig.update_layout(yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig, theme = None)
    with tab2:
        fig = px.choropleth(country_sales, locations = 'CountryISO3',
                    color = 'Revenue',
                    color_continuous_scale = 'viridis',
                    title = 'Revenue Distributions',
                    hover_name = 'Country',
                    hover_data = {'CountryISO3':False})
        # fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig, theme = None)

country()

