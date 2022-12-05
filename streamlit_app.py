# pip freeze > requirements.txt
import time
import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
import webbrowser
from PIL import Image
import database as db

st.set_page_config(
    page_title="Datvilla",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.facebook.com/profile.php?id=100008279142274',
        'Report a bug': "https://www.facebook.com/profile.php?id=100008279142274",
        'About': "# if you have something to report dm https://www.facebook.com/profile.php?id=100008279142274"
    }
)


col1, col2, col3 = st.columns((2,4,1))
with col1:
    st.image(Image.open('dark_logo.png'))
    # if st.theme():
    #     st.image(Image.open('logo.png'))
    # else:
    #     st.image(Image.open('dark_logo.png'))

# st.plotly_chart(fig.update_layout(theme))
with col2:
    st.header(' ')
    st.header('Knowledge Represent')
    st.markdown('Your choice, your comfort')
# with col3: 
    # st.title('Represent')
# st.markdown('# 30 days of NNN is over')

# df = pd.read_csv('Database.csv')
# st.write(df)

with st.form("my_form"):
    quan = st.multiselect(
        'Quận',
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 
        'Tân Bình', 'Bình Tân', 'Tân Phú', 'Bình Thạnh', 'Gò Vấp', 'Phú Nhuận',
        'Hóc Môn', 'Bình Chánh', 'Nhà Bè', 'Củ Chi'))

    submitted = st.form_submit_button("Next")

if not quan and submitted==True:
    st.warning("Hãy chọn quận!!",icon="⚠️")

with st.expander('Bộ lọc'):
        # filter = st.button('Bộ lọc')
    if quan:
        # with st.form("price"):
            # st.write('Quận đã chọn: ', ', '.join(quan))   
            # st.text("Filter")
        money = st.slider('Giá tiền (triệu/m²)',0, 200, (0, 50))
        # st.write(money)
        area = st.slider('Diện tích m²', 0, 500, (0, 70))
        col1, col2 = st.columns((1,1))
        with col1:
            sleep = st.selectbox('Số phòng ngủ', (1,2,3,4,5))
        with col2:
            vs = st.selectbox('Số phòng vệ sinh', (1,2,3))
    search = st.button("Search")
    if search:
        # st.write('Quận đã chọn: ', ', '.join(quan))
        
        user = db.fetch_all_apartments()
        for i in quan:
            st.header('Quận ' + i)
            dis = [us for us in user if us['districts']==i]
            df = pd.DataFrame(dis)  
            
            # df = df[df['rates'] <= str(money[1])]
            # df = df[df['rates'] >= str(money[0])]
            # df = df[df['areas'] <= str(area[1])]
            # df = df[df['areas'] >= str(area[0])]
            # df = df[df['wc'] <= str(vs+1)]
            # df = df[df['bedrooms'] >= str(sleep)]
            if df.empty:
                st.write('Không có kết quả phù hợp!')

            
            for i in range(len(df.iloc[:])):
                d = df.iloc[i,:]
                st.subheader(d['key'])
                st.info(d['addresses'] + ", phường " + d['wards'] + ", quận " + d['districts'] + ', Tp.HCM', icon="🏢")
                col1, col2, col3, col4 = st.columns((1.3,1,1,1.5))
                with col1:
                    st.info(d['areas'] + ' m²',icon='🛋')
                with col2:
                    st.success(d['bedrooms'],icon='🛏️')
                with col3:
                    st.warning(d['wc'],icon='🛁')
                with col4:
                    st.error(d['rates'] + " triệu/m²",icon='💲')
            # pd  
        # st.write(user) 
                # st.select_slider("Displayed values:", ["Normalized", "Absolute"])

# with col2:
#     if quan:
#         with st.form('area'):
#             with st.expander("filter"):
#             # st.text("Filter")
#                 money = st.slider('Diện tích (m²)', 0, 200, (0, 50))
#             search = st.form_submit_button("Search")
#             if search:
#                 st.write('Quận đã chọn: ', ', '.join(quan))
#             # st.select_slider("Displayed values:", ["Normalized", "Absolute"])

url = 'https://youtu.be/'
url_= 'dQw4w9WgXcQ'

if st.button('_do not click_ **this**'):
    webbrowser.open_new_tab(url+url_)
    st.caption('i told ya')



