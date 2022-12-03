# pip freeze > requirements.txt
import time
import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
import webbrowser
from PIL import Image

col1, col2, col3 = st.columns((2,4,1))
with col1:
    st.image(Image.open('logo.png'))
with col2:
    st.header(' ')
    st.header('Knowledge Represent')
    st.markdown('Your choice, your comfort')
# with col3: 
    # st.title('Represent')
st.markdown('# 30 days of NNN is over')

with st.form("my_form"):
    # st.write("Inside the form")

#    # Every form must have a submit button.
#      submitted = st.form_submit_button("???")
#      if submitted:
#           st.write("slider", slider_val, "checkbox", checkbox_val)
    option = st.selectbox(
        'Quận',
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 
        'Tân Bình', 'Bình Tân', 'Tân Phú', 'Bình Thạnh', 'Gò Vấp', 'Phú Nhuận',
        'Hóc Môn', 'Bình Chánh', 'Nhà Bè', 'Củ Chi'))

    st.write('You selected:', option)
    if option == '1':
        st.write("ho ho ho")
     
    # image = Image.open('dalat.jpg')
    # st.image(image, caption='Sunrise by the mountains')
    # submitted = st.form_submit_button("Search")
    submitted = st.form_submit_button("Search")
    if submitted:
        st.write("your mom is a hoe")
# st.write("Outside the form")
# # submitted = st.button('submit')

url = 'https://youtu.be/dQw4w9WgXcQ'

if st.button('do not click this'):
    webbrowser.open_new_tab(url)


