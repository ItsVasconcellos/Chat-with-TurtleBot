import streamlit as st
import re
import os

intentions = {
    'Secretária': 'Me direcionando para a secretária',
    'Laboratório': 'Indo para o laboratório ',
    '': ''
}


st.title("Welcome to the chatbot 3000!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])