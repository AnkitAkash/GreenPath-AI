import streamlit as st
from PIL import Image
from utils.chatbot import analyze_image

st.set_page_config(page_title="Nutrition Analysis", page_icon="🍏")

st.title("🍏 Nutrition & ESG Rating Analyzer")
st.write("Upload a product image to instantly analyze its nutritional value and Environmental, Social, and Governance (ESG) rating. Get insights on its health benefits, carbon footprint, sustainability impact, and ethical sourcing to make informed, climate-conscious food choices.")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Analyzing..."):
        analysis_result = analyze_image(uploaded_image)

    st.subheader("ESG Rating:")
    st.write(analysis_result)  # ✅ Short, concise result

st.page_link("app.py", label="Back to Home", icon="🏡")
