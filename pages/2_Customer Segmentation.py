import streamlit as st
import pandas as pd
import numpy as np
import time

import folium
import branca.colormap as cm
from streamlit_folium import folium_static
import plotly.express as px
# st.set_page_config(layout="wide")
st.title('Customer Segmentation')

st.markdown(
    """
    In this section, I will present the visualization of the clustering results using k-means.
    """
)

df = pd.read_csv('dataset/rfm_modified.csv')

@st.cache_data
def show_data_RFM():
    st.write(df)
if st.checkbox('Show Data RFM!'):
    show_data_RFM()


# Filter the DataFrame to include only cluster 0
df_cluster_0 = df[df['Cluster'] == 'cluster_0']

# Filter the DataFrame to include only cluster 1
df_cluster_1 = df[df['Cluster'] == 'cluster_1']

# Filter the DataFrame to include only cluster 2
df_cluster_2 = df[df['Cluster'] == 'cluster_2']

# Filter the DataFrame to include only cluster 3
df_cluster_3 = df[df['Cluster'] =='cluster_3']

custom_color_map = {
    'cluster_0': '#ef476f',
    'cluster_1': '#ffd166',
    'cluster_2': '#06d6a0',
    'cluster_3': '#118ab2'
}

rfm_select = st.selectbox('Select cluster:', ['All', 'Cluster 0','Cluster 1','Cluster 2','Cluster 3'])
@st.cache_data
def visualize_rfm(rfm_select):

    if rfm_select == 'All':
        fig = px.scatter_3d(df, x='Frequency', y='Recency', z='Monetary',
                    color='Cluster', hover_name='CustomerNo',
                    color_discrete_map=custom_color_map, width=850, height=650, title = "All Cluster")
        st.plotly_chart(fig, theme = None)
        # fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    elif rfm_select == 'Cluster 0': 
        fig = px.scatter_3d(df_cluster_0, x='Frequency', y='Recency', z='Monetary',
                    color='Cluster', hover_name='CustomerNo', title = "Cluster 0",
                    color_discrete_map=custom_color_map, width=850, height=650)
        # fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig, theme = None)
    elif rfm_select == 'Cluster 1': 
        fig = px.scatter_3d(df_cluster_1, x='Frequency', y='Recency', z='Monetary',
                    color='Cluster', hover_name='CustomerNo', title = "Cluster 1",
                    color_discrete_map=custom_color_map, width=850, height=650)
        # fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig, theme = None)
    elif rfm_select == 'Cluster 2': 
        fig = px.scatter_3d(df_cluster_2, x='Frequency', y='Recency', z='Monetary',
                    color='Cluster', hover_name='CustomerNo', title = "Cluster 2",
                    color_discrete_map=custom_color_map, width=850, height=650)
        # fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig, theme = None)
    else:
        fig = px.scatter_3d(df_cluster_3, x='Frequency', y='Recency', z='Monetary',
                    color='Cluster', hover_name='CustomerNo', title = "Cluster 3",
                    color_discrete_map=custom_color_map, width=850, height=650)
        # fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig, theme = None)

visualize_rfm(rfm_select)

# Calculate the percentage of customers in each cluster
cluster_count = df['Cluster'].value_counts(normalize=True).reset_index()
cluster_count.columns = ['Cluster', 'percentage']
cluster_count['percentage'] *= 100

st.subheader('Cluster Distribution Percentage(%)')
@st.cache_data
def rfm_percentage():
    fig = px.bar(cluster_count, x='Cluster', y='percentage',
             text=cluster_count['percentage'].apply(lambda x: f'{x:.2f} %'),
             color='Cluster',
             title='Percentage of Customer by Cluster',
             color_discrete_map=custom_color_map, width=800, height=600)
    fig.update_layout(xaxis_title='Cluster', yaxis_title='Percentage')
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig, theme = None)
rfm_percentage()

st.markdown(
    """ 
    # Cluster Characteristics
    ### Cluster 0 -> Frequent High Spender
    Characteristics:
    - Customers in this cluster frequently make purchases and tend to spend relatively large amounts.
    - They have recently made a purchase (low Recency value), indicating that they are very active.

    ### Cluster 1 -> Regular Shopper
    Characteristics:
    - Customers in this cluster have moderate transaction values and make purchases with moderate frequency.
    - They have a higher recency value compared to some other clusters, indicating that they may not have made a recent purchase but are still fairly active.


    ### Cluster 2 -> Loyal High Spender
    Characteristics:
    - Customers in this cluster are the most valuable, with very high transaction values and very frequent purchases.
    - They have recently made a purchase, indicating a very high level of activity

    ### Cluster 3 -> Inactive Low Spender
    Characteristics:
    - Customers in this cluster have low transaction values and very low purchase frequency.
    - They have not made a recent purchase, indicating that they may be inactive.

"""
)









