import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Description",
)

st.markdown("# Welcome to My Final Project! 👋")

st.markdown(
    """
    ## Project Background
    This company is a UK-based e-commerce business that has been selling gifts and homewares for adults and children through its website since 2007. The dataset used includes sales transactions for one year (December 2018 to December 2019). The company needs to identify potential customer segments to better and more efficiently target its market. This information will ensure that all future campaigns and marketing efforts are directed towards customers who are most likely to make purchases.

    ## Objective
    To identify segments within the current customer base, we will use exploratory data analysis (EDA) and the k-means clustering algorithm. Then, we will determine the best customer segment using the RFM framework. Finally, we will propose several relevant business recommendations that cater to the characteristics of the best customer segment.


    **👈 Select any pages from the sidebar** for more detail!

"""
)

df = pd.read_csv('dataset\Sales Transaction v.4a.csv')

st.markdown("## Description of Dataset")
@st.cache_data
def show_dataset():
    st.write(df)
if st.checkbox('Show Data!'):
    show_dataset()

st.markdown(
    """ 
    - TransactionNo: a six-digit unique number that defines each transaction. The letter “C” in the code indicates a cancellation.
    - Date: the date when each transaction was generated.
    - ProductNo: a five or six-digit unique character used to identify a specific product.
    - Product: product/item name.
    - Price: the price of each product per unit in pound sterling (£).
    - Quantity: the quantity of each product per transaction. Negative values related to cancelled transactions.
    - CustomerNo: a five-digit unique number that defines each customer.
    - Country: name of the country where the customer resides
"""
)