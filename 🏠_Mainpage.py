import streamlit as st
import streamlit.components.v1 as components
from constant import *

st.set_page_config(page_title="Main Page", page_icon="🏠", layout="wide",initial_sidebar_state="collapsed") 

margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
    menu()

    #sidebar --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    with st.sidebar:
        st.success("Select a page above.")
        
    #main page --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    st.header("About Me",divider='blue')

    col1, col2, col3 = st.columns([1.3 ,0.2, 1])

    with col1:
        st.write(info['brief'])
        st.markdown(f"######  🔘Name: {info['name']}")
        st.markdown(f"######  🔘Location: {info['location']}")
        st.markdown(f"######  🔘Interest: {info['interest']}")
        st.markdown(f"######  🔘Linkedin: {linkedin_link}")
        
        # with open("src/JasheshKanzariya.pdf", "rb") as file:
        #     pdf_file = file.read()

        # st.download_button(
        #     label="Download my :blue[resume]",
        #     data=pdf_file,
        #     file_name="JasheshKanzariya",
        #     mime="application/pdf")

    with col3:
        st.image("src/image.jpg", width=360)

    # skills --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    st.subheader("My :blue[skills] ⚒️",divider='blue') #,divider='rainbow'

    def skill_tab():
        rows,cols = len(info['skills'])//skill_col_size, skill_col_size
        skills = iter(info['skills'])
        if len(info['skills'])%skill_col_size!=0:
            rows+=1
        for x in range(rows):
            columns = st.columns(skill_col_size)
            for index_ in range(skill_col_size):
                try:
                    columns[index_].button(next(skills))
                except:
                    break
    with st.spinner(text="Loading section..."):
        skill_tab()
