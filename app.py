import streamlit as st
import requests

import streamlit as st
from streamlit.components.v1 import html

# Page Configuration
st.set_page_config(page_title="Personal AI Assistant", page_icon="🧠", layout="centered")

# Custom CSS for a cleaner look
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .title-container {
            text-align: center;
            padding: 2rem 1rem;
        }
        .title-container h1 {
            font-size: 3rem;
            color: #333;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #666;
            margin-top: -1rem;
        }
        .chat-container {
            margin-top: 3rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title section
st.markdown("""
<div class="title-container">
    <h1>🧠 Personal AI Assistant</h1>
    <p class="subtitle">Chat with your locally running LLM in real time</p>
</div>
""", unsafe_allow_html=True)



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# # Input box
# user_input = st.chat_input("Say something...")


# Exit
st.markdown("""
<div class="title-container">
    <a href="http://127.0.0.1:8000/" style="text-decoration: none; color: blue;">⬅ Go Back</a>
</div>
""", unsafe_allow_html=True)




# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle user input
# if user_input:
#     # Show user's message
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     with st.chat_message("user"):
#         st.markdown(user_input)

    # Send to Ollama
    # with st.chat_message("assistant"):
    #     with st.spinner("Thinking..."):
    #         response = requests.post("http://localhost:11434/api/generate", json={
    #             "model": "llama3.2",
    #             "prompt": user_input,
    #             "stream": False,
    #             "options": {
    #                 "num_predict": 5000  # Limit the number of tokens in response
    #             }
    #         })
    #         reply = response.json()["response"]
    #         st.markdown(reply)
    #         st.session_state.messages.append({"role": "assistant", "content": reply})

user_input = st.text_input("Say something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send to Ollama
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = requests.post("http://localhost:11434/api/generate", json={
                "model": "llama3.2",
                "prompt": user_input,
                "stream": False,
                "options": {
                    "num_predict": 5000  # Limit the number of tokens in response
                }
            })
            reply = response.json()["response"]
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

