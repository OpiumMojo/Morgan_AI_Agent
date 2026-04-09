import streamlit as st
import google.generativeai as genai

# Configuration
st.set_page_config(page_title="MSU CS Agent", page_icon="🐻")
genai.configure(api_key="AQ.Ab8RN6JZnsO_BjOlCarV0np-vt7MNwCn-N6AuT-S7rjccZK0PQ") # <--- PASTE KEY HERE

# System Prompt
instructions = """
You are the Morgan State University CS AI Agent. 
Support students with advising (COSC courses) and learning computer science concepts.
"""

model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=instructions)

# Sidebar for Project Info
with st.sidebar:
    st.title("MSU Project Info")
    st.info("Focus: Freshmen & Sophomore Academic Support")

# Chat UI Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})