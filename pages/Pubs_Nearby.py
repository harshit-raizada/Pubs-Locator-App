import pandas as pd
import numpy as np
import os
import streamlit as st

FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1, os.pardir)

dir_of_interest = os.path.join(FILE_DIR, "resources")
DATA_PATH1 = os.path.join(dir_of_interest, "open_pubs.csv")

df = pd.read_csv(DATA_PATH1)

st.write("<h1 style='text-align: center; color: #FFD700;'>Welcome to Pub Locator App🍺</h1>", unsafe_allow_html=True)

df.columns = ['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority']

df.replace('\\N', np.nan, inplace = True)
df.dropna(inplace = True)

df.latitude = df.latitude.astype(float)
df.longitude = df.longitude.astype(float)

col1, col2 = st.columns(2)

with col1:
    lat = st.number_input(label = 'Enter Latitude', value = 55.2)

with col2:
    lon = st.number_input(label = 'Enter Longitude', value = -3.5)
    
points = np.array((lat, lon))

arr = np.array([df['latitude'], df['longitude']]).T

dist = np.sum((arr - points)**2, axis = 1)

df['distance'] = dist

nearest_value = st.slider(label = 'How many nearby pubs you want to see', min_value = 1, max_value = 10, value = 5)

data = df.sort_values(by = 'distance', ascending = True)[:nearest_value]

st.subheader(f'Nearest {nearest_value} Pubs:')

st.map(data = data, zoom = None, use_container_width = True)

st.table(data[['name', 'address', 'local_authority']])

st.markdown("<hr>", unsafe_allow_html=True)
st.write("Data Source: https://www.getthedata.com/open-pubs")