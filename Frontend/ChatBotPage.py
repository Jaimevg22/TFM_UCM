import streamlit as st
from Frontend.FrontendFunctions import update_data, get_id_from_video_url

def get_response(prompt : str) -> str:
    #Aqui hay que meter la inferencia del llama o lo que sea
    return "respuesta"
    
def chat_bot():

    chat_container = st.container(height=700)
    prompt = st.chat_input("What is up?")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with chat_container.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt:
        # Display user message in chat message container
        chat_container.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = get_response(prompt)
        # Display assistant response in chat message container
        with chat_container.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

# def chat_bot():

#     chat_container = st.container(height=300)
#     prompt = st.chat_input("What is up?")

#     if 'messages' not in st.session_state:
#         st.session_state.messages = []

#     def responder_chatbot(pregunta):
#         return "respuesta"


#     with st.container():
#         for msg in st.session_state['messages']:
#             if msg['role'] == 'user':
#                 st.write(f"**Tú:** {msg['content']}")
#             else:
#                 st.write(f"**Chatbot:** {msg['content']}")

#     with st.container():
#         user_input = st.text_input("Escribe tu mensaje:")

#         if st.button("Enviar"):
#             if user_input:
#                 # Guardar el mensaje del usuario
#                 st.session_state['messages'].append({"role": "user", "content": user_input})
                
#                 # Obtener la respuesta del chatbot
#                 respuesta = responder_chatbot(user_input)
#                 st.session_state['messages'].append({"role": "bot", "content": respuesta})
