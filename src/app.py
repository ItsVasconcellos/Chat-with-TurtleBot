import streamlit as st
import re
import random
import time


intentions = {
    'Secretaria': 'Me direcionando para a secretária',
    'Laboratório': 'Indo para o laboratório ',
    '': ''
}

def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("Bem vindo ao chatbot3000!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display chatbot response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())   
    
    st.session_state.messages.append({"role": "assistant", "content": response})