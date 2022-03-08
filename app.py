import pandas as pd
import streamlit as st


import get_data as data

st.set_page_config(page_title="WebScrapping - PY101", page_icon="🛒", layout="wide")
st.image("https://unpackai.github.io/unpackai_logo.svg")
st.title("WebScrapping of Lego Prices around the world 🌏")
st.write("*by <Abby sweet>*")
st.write([1,2,3])
# st.write("a1,a2,a3")
st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cnet.com%2Ftech%2Fmobile%2Fbest-phone-to-buy%2F&psig=AOvVaw1aq9EOcWtkoRg2rDiNuqP5&ust=1646830170911000&source=images&cd=vfe&ved=2ahUKEwiSp4HMxrb2AhWKHjQIHXfBCUoQjRx6BAgAEAk")

def launch_balloons_and_snow():
  st.ballons()
  st.snow()

st.button("Launch balloons", on_click=st.balloons)
st.button("Make it snow", on_click=st.snow)
st.button("Balloons in the snow", on_click=launch_and_snow)