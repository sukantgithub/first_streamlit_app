import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title("My Parents new heathy diner.")

streamlit.header("Breakfast favorites")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-range Egg")
streamlit.text("🥑🍞 Avacado Toast ")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits: " , list(my_fruit_list.index), ['Avocado','Strawberries'])
if fruits_selected == '':
  streamlit.dataframe(my_fruit_list)
else:
  fruits_to_show = my_fruit_list.loc[fruits_selected]
  streamlit.dataframe(fruits_to_show)

