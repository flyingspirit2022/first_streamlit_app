import streamlit
import pandas

streamlit.title('My Mom new healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🧆Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚Hard Boiled free range egg')
streamlit.text('🥑Avocado toast')
streamlit.header('🍌🍓 Build your own smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)
