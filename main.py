import streamlit as st
import pandas
st.set_page_config(layout='wide')

col1,col2 = st.columns(2)


with col1:
    st.image("data/images/image.jpeg")

with col2:
    st.title('Viacheslav Tkachenko')
    content = """
        Hi, I am Viacheslav! I am a Python programmer!
    """
    st.write(content)

content2 = """
    Below you can find some apps I have built in Python.Feel free to contact me!
"""

st.write(content2)

col3,empty_col,col4=st.columns([1.5,0.7 ,1.5])
df = pandas.read_csv("data/data.csv",sep=';')
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image('data/images/'+row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('data/images/'+row['image'])