import pandas as pd
import numpy as np
import os
import streamlit as st
import folium
from streamlit_folium import folium_static

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

searchType = st.radio('Filter By:', ('Postal Code', 'Local Authority'))

if searchType == 'Postal Code':
    search_list = sorted(df['postcode'].unique())
else:
    search_list = sorted(df['local_authority'].unique())

select_value = st.selectbox(f'Select a {searchType}:', search_list)

if searchType == 'Postal Code':
    filtered = df[df['postcode'] == select_value]
else:
    filtered = df[df['local_authority'] == select_value]

st.write(f'Showing results for {len(filtered)} pubs in {select_value}:')
st.dataframe(filtered)

map = folium.Map(location = [filtered['latitude'].mean(), filtered['longitude'].mean()], zoom_start = 12)

for index, row in filtered.iterrows():
    folium.Marker(location = [row['latitude'], row['longitude']], popup = row['name']).add_to(map)

folium_static(map)

st.markdown("<hr>", unsafe_allow_html=True)
st.write("Data Source: https://www.getthedata.com/open-pubs")