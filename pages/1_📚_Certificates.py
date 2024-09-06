import streamlit as st
import streamlit.components.v1 as components
from constant import *
from PIL import Image

st.set_page_config(page_title="Certificates", page_icon="📚", layout="wide",initial_sidebar_state="collapsed")
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
    menu()
    st.header("📚 Certificates")
    st.write("")
    
    for certificate in certificates:

        st.subheader(certificate["title"], divider="blue")
        st.write(f"**Organization**: {certificate['organization']}")
        st.write(f"**Date**: {certificate['date']}")
        
        
        # Display the certificate image
        img = Image.open(certificate['image'])
        st.image(img, caption=certificate["title"], use_column_width=True)

