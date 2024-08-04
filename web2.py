import streamlit as st
from streamlit_theme import st_theme
import datetime

st.write("Время записи более 1:30 можно производить только на выходных")
option = st.selectbox(
"Сколько времини будет висти запесь",
("0:30", "1:00", "1:30", "2:00", "2:30"),
index=True,
placeholder="Выберете врямя",
)

st.write("Выберете дату")
d = st.date_input(" ", value=None)

st.write("Выберете время в формате 24")
t = st.time_input(" ", datetime.time(10, 40))

st.write("Видите актуальный номер телефона для связи в вацап")
namber = st.text_input(" ", "+78003553555")

if (t < 10):
   st.error('нельзя записатся раньше 10:00', icon="🚨")
if (t > 10):
   st.error('нельзя записатся поже 19:00', icon="🚨")

if st.button("Подвердить"):
   print(option, "/", d, "/", t, "/", namber)