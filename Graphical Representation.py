import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import streamlit as st
import streamlit_option_menu as option_menu

#read the dataset
data= pd.read_csv("C:/Users/saisr/OneDrive/Desktop/3rd sem/Adv Python/ESE/WomensClothingE-CommerceReviews.csv")
st.title("Visual Representation of Women's Clothing E-Commerce Reviews Dataset")
st.subheader("Insights:")
st.write(data.describe())

st.subheader("Data Set Exploration through Graphs:")
st.write("")
feature_x = st.selectbox("Select a feature for x axis", data.columns)
feature_y = st.selectbox("Select a feature for y axis", data.columns)
feature_z = st.selectbox("Select a feature for z axis", data.columns)

# st.subheader("Scatter Plot")
fig, ax = plt.subplots()

st.subheader("Scatter Plot")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x=feature_x, y=feature_y)
plt.xlabel(feature_x)
plt.ylabel(feature_y)
# plt.zlabel(feature_z)
plt.title("Scatter Plot")
st.pyplot(fig)

# Bar plot
st.subheader("Bar Plot")
fig, ax = plt.subplots()
sns.countplot(data=data, x=feature_x)
plt.xlabel(feature_x)
plt.ylabel("Count")
plt.title("Bar Plot")
st.pyplot(fig)


    














