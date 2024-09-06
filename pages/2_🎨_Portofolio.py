import streamlit as st
import streamlit.components.v1 as components
from constant import *
import pandas

# page config ----------------------------------------------------------------
st.set_page_config(page_title="Portfolio", page_icon="🎨", layout="wide",initial_sidebar_state="collapsed")
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
   menu()

   st.header("🎨 Portfolio",divider='rainbow')

   # page functions ----------------------------------------------------------------
   def Portfolio_component(header, content):
      st.subheader(header, divider='grey')
      st.write(content)
   
   col3, em_col, col4 = st.columns([1.5, 0.5, 1.5])

   df = pandas.read_csv("data.csv", sep = ";")
   with col3:
      for index, row in df[:6].iterrows():
         
         st.header(row["title"])
         st.write(row["description"])
         st.image("images/" + row["image"])
         st.link_button(f"Project Demo: {row['title']}", url=row['link'])
         st.markdown(
            """
            <hr style='border: 2px solid blue; margin: 20px 0;'>
            """,
            unsafe_allow_html=True
        )
   
   with col4:
      for index, row in df[6:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.link_button(f"Project Source Code: {row['title']}", url=row['link'])
        st.markdown(
            """
            <hr style='border: 2px solid blue; margin: 20px 0;'>
            """,
            unsafe_allow_html=True
        )
  