import streamlit as st
from send_email import email_send

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button('Submit')
    if button:
        try:
            email_send(message)
            st.info("Your mail send saccesfully")
        except:
            print('Not send !')
