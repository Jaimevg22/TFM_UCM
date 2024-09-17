import streamlit as st
from Frontend.FrontendFunctions import update_data
from src.rag_querying import *
from src.audio import WORK_DIR

print("QA model is going to load")
setup_qa_model(embedding_model="BAAI/bge-base-en-v1.5", ollama_model="llama3.1", ollama_opt=True)
print("[+] QA model loaded")

def load_query_engine():
    print("[+] Creating the query engine")
    return create_query_engine_from_directory(f"{WORK_DIR}/data/documents")

# Load the query engine when the app starts
if 'query_engine' not in st.session_state:
    st.session_state.query_engine = load_query_engine()
    
def chat_bot():

    chat_container = st.container(height=700)

    if st.button("Reload Query Engine"):
            st.session_state.query_engine = load_query_engine()
            st.success("Query engine reloaded!")

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

        response, _  = query_vector_store(st.session_state.query_engine, prompt)
        # Display assistant response in chat message container
        with chat_container.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
