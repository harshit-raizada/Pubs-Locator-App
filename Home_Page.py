import streamlit as st

st.write("<h1 style='text-align: center; color: #FFD700;'>Welcome to Pub Locator App🍺</h1>", unsafe_allow_html=True)

st.subheader(':green[Lets assume I am on a vacation in the United Kingdom with my friends:surfer:]') 
st.subheader(':red[For fun, we decide to go to the Pubs nearby for some drinks]🍺')
st.subheader(':blue[Google Map is down because of some issues]:world_map:')
st.subheader(':violet[Myself being a tech savvy, I want to create an application that works similar to Google Maps]:desktop_computer:')

st.subheader(":green[Connect with me on:]")

col1, col2 = st.columns(2)

with col1:
    st.subheader("[LinkedIn](https://www.linkedin.com/in/harshit-raizada/)")
with col2:
    st.subheader("[GitHub](https://github.com/harshit-raizada)")

st.text(" ")
st.text(" ")

st.write('By: :orange[Harshit Raizada]')