import streamlit as st
from difflib import get_close_matches


patterns_responses = {
    r'secretaria': 'Me direcionando para a secretária',
    r'laboratório': 'Indo para o laboratório',
    r'biblioteca': 'Indo para a biblioteca'
}

default_response = "Não entendi o que foi dito, você poderia refrasear, por favor?"

def get_response(user_input):
    response = get_close_matches(user_input, patterns_responses.keys() , n=3, cutoff=0.6)
    if response != []:
        return patterns_responses[response[0]]
    return default_response

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
    
    # Get chatbot response
    response = get_response(prompt)
    
    # Display chatbot response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})