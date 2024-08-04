import streamlit as st
from streamlit_theme import st_theme

st.image(r"imeg\baraban\1.jpg", caption="Барабаны", width=320)
st.video(r".\video\baraban\1.mp4")
st.image(r"imeg\gitara\1.jpg", caption="Гитара", width=320)
st.image(r"imeg\pionino\1.jpg", caption="Фортопиано", width=320)
st.image(r"imeg\Vokal\1.jpg", caption="Вокал", width=320)
st.video(r".\video\vokal\1.mp4")


if st.button("записатся"):
    print("ok")
         

selected = st.feedback("stars")
if selected is not None:
    print(selected + 1)
