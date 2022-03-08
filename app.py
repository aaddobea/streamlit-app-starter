import pandas as pd
import streamlit as st


import get_data as data

st.set_page_config(page_title="WebScrapping - PY101", page_icon="🛒", layout="wide")
st.image("https://unpackai.github.io/unpackai_logo.svg")
st.title("WebScrapping of Lego Prices around the world 🌏")
st.write("*by <Abby sweet>*")
st.write([1,2,3])
# st.write("a1,a2,a3")
st.image("https://cdn.pixabay.com/photo/2022/01/15/02/07/windows-6938478__340.jpg")

def launch_balloons_and_snow():
  st.ballons()
  st.snow()

st.button("Launch balloons", on_click=st.balloons)
st.button("Make it snow", on_click=st.snow)
st.button("Balloons in the snow", on_click=launch_and_snow)

#fruit = st.radio("Fruit type",["Apples","Pears","Lemons])
#number_of_fruits = st.slider(f"Number of {fruit}",1,35)  
#st.write("There are",number_of_fruits, fruit)
#st.write(number_of_fruits/20)