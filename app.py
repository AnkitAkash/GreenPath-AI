import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into system environment

# Set up the page
st.set_page_config(page_title="GreenPath AI Hub", page_icon="🌿", layout="wide")

# Custom CSS to set an image as the background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E9F5E1;  /* Light green background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌿 Welcome to GreenPath AI Hub")
st.write("Choose an option below:")

# Define image paths
nutrition_img_path = "assets/images/nutrition_analysis.png"
travel_img_path = "assets/images/greenpath.png"
diet_img_path = "assets/images/diet_plan.png"
chatbot_img_path = "assets/images/chatbot.png"
climate_news_img_path = "assets/images/climate_news.png"  # ✅ New Image for Climate News

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if os.path.exists(nutrition_img_path):
        st.image(nutrition_img_path, use_container_width=True)
    else:
        st.warning("⚠️ Nutrition image not found. Please check the assets folder.")
    
    st.markdown("### 🍏 Nutrition & ESG Rating")
    if st.button("Go to Nutrition Analysis"):
        st.switch_page("pages/nutrition_analysis.py")

with col2:
    if os.path.exists(travel_img_path):
        st.image(travel_img_path, use_container_width=True)
    else:
        st.warning("⚠️ GreenPath image not found. Please check the assets folder.")
    
    st.markdown("### 🚗 GreenPath Travel Assistant")
    if st.button("Go to GreenPath Assistant"):
        st.switch_page("pages/greenpath_assistant.py")

with col3:
    if os.path.exists(diet_img_path):
        st.image(diet_img_path, use_container_width=True)
    else:
        st.warning("⚠️ Diet Plan image not found. Please check the assets folder.")
    
    st.markdown("### 🥗 Personalized Diet Plan")
    if st.button("Go to Diet Plan"):
        st.switch_page("pages/diet_plan.py")

with col4:
    if os.path.exists(chatbot_img_path):
        st.image(chatbot_img_path, use_container_width=True)
    else:
        st.warning("⚠️ AI Chatbot image not found. Please check the assets folder.")
    
    st.markdown("### 🤖 AI Carbon Footprint Chatbot")
    if st.button("Go to AI Chatbot"):
        st.switch_page("pages/carbon_chatbot.py")

with col5:
    if os.path.exists(climate_news_img_path):
        st.image(climate_news_img_path, use_container_width=True)
    else:
        st.warning("⚠️ Climate News image not found. Please check the assets folder.")
    
    st.markdown("### 🌍 Climate News Updates")
    if st.button("Go to Climate News"):
        st.switch_page("pages/climate_news.py")
