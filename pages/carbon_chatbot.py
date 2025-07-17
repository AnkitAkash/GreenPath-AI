import streamlit as st
from utils.chatbot import ask_sustainability_ai

st.set_page_config(page_title="AI Carbon Footprint Chatbot", page_icon="🤖")

# Custom CSS to set an image as the background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E9F5E1;  /* You can change this to any shade of green you prefer */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 AI Chatbot for Carbon Footprint Advice")
st.write("Ask a question about reducing your carbon footprint, and get **a short, actionable tip**.")

question = st.text_input("Ask a question (e.g., 'How can I reduce my travel emissions?')")

if st.button("💬 Get AI Advice"):
    if question:
        response = ask_sustainability_ai(question)
        st.success(response)  # ✅ Now returns a short, clear response
    else:
        st.error("Please enter a question before asking AI.")

st.page_link("app.py", label="🏠 Back to Home")
