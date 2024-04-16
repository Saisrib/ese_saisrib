import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.title("Analysis on Women's Clothing E-Commerce Reviews")
st.write("""This is a Women’s Clothing E-Commerce dataset revolving around the reviews written by customers. Its
nine supportive features offer a great environment to parse out the text through its multiple dimensions.
Because this is real commercial data, it has been anonymized, and references to the company in the
review text and body have been replaced with retailer
Content
This dataset includes 23486 rows and 10 feature variables. Each row corresponds to a customer review,
and includes the variables:""")
data= pd.read_csv("C:/Users/saisr/OneDrive/Desktop/3rd sem/Adv Python/ESE/WomensClothingE-CommerceReviews.csv")

st.subheader("Introduction:")
st.write("")
st.subheader("Dataset:")
st.write(data)  # Displaying the dataset


