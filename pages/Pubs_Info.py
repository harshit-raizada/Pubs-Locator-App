import pandas as pd
import numpy as np
import os
import streamlit as st
from matplotlib import image

FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1, os.pardir)

dir_of_interest = os.path.join(FILE_DIR, "resources")
DATA_PATH1 = os.path.join(dir_of_interest, "open_pubs.csv")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "pub.jpg")
img = image.imread(IMAGE_PATH)

df = pd.read_csv(DATA_PATH1)

st.write("<h1 style='text-align: center; color: #FFD700;'>Welcome to Pub Locator App🍺</h1>", unsafe_allow_html=True)

df.columns = ['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority']

df.replace('\\N', np.nan, inplace = True)
df.dropna(inplace = True)

df.latitude = df.latitude.astype(float)
df.longitude = df.longitude.astype(float)

st.image(img)

st.write("I have created an application that identifies nearby pubs in United Kingdom (U.K).")
st.write("You can enter the desired coordinates i.e Longitude & Latitude to obtain nearby pub areas.")
st.write(f"There are **{len(df)}** pub locations.")
st.write(f"There are **{len(df['local_authority'].unique())}** local authorities that offer wines, beer etc.")
st.write("County Durham is the most popular local authority in U.K with 680 branches.")

st.write("<h1 style='text-align: center; color: #FFD700;'>Pubs Random Data!🍺</h1>", unsafe_allow_html=True)
st.write(df.sample(25))

st.write("<h1 style='text-align: center; color: #FFD700;'>Statistics About Data 📈</h1>", unsafe_allow_html=True)
st.write(df.describe().T)

st.markdown("<hr>", unsafe_allow_html=True)
st.write("Data Source: https://www.getthedata.com/open-pubs")