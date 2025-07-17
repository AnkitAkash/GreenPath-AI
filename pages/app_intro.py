import streamlit as st

st.set_page_config(page_title="🌿 GreenPath AI Hub - Introduction", page_icon="🌍", layout="wide")

# -------------------- 🌍 Styling -------------------- #
st.markdown(
    """
    <style>
        .big-title { text-align: center; font-size: 40px; font-weight: bold; color: #2E8B57; }
        .sub-text { text-align: center; font-size: 20px; color: #555; }
        .highlight { font-size: 22px; font-weight: bold; color: #228B22; }
        .section { padding: 20px; border-radius: 10px; background-color: #F5F5F5; margin-bottom: 20px; text-align: center; }
        .button { 
            display: block; 
            width: 250px; 
            text-align: center; 
            margin: 0 auto; 
            background-color: #2E8B57; 
            border: none; 
            color: white; 
            padding: 12px 20px; 
            font-size: 18px; 
            border-radius: 8px; 
            cursor: pointer; 
            transition: 0.3s; 
        }
        .button:hover { background-color: #228B22; }
        .stApp { background-color: #E9F5E1; } /* Light green background */
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- 🌍 Welcome Section -------------------- #
st.markdown('<p class="big-title">🌍 Welcome to GreenPath AI Hub!</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">An AI-powered sustainability platform to make eco-friendly choices.</p>', unsafe_allow_html=True)

st.image("assets/images/app_intro.png", use_container_width=True)

# -------------------- 🌱 About EcoAI Hub -------------------- #
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🌱 What is GreenPath AI Hub?")
st.write("""
GreenPath AI Hub leverages **AI technology** to help users **track, analyze, and optimize** their daily activities for a **greener planet**.
With AI-powered insights, you can:
- 🚗 **Analyze your transportation carbon footprint**
- 🥗 **Get a sustainability rating for your diet**
- 🌱 **Receive eco-friendly lifestyle suggestions**
""")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------- ❓ Why It Matters -------------------- #
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("❓ Why Does This Matter?")
st.write("""
- 🌍 **Transportation contributes 25% of global CO₂ emissions.**  
- 🥗 **Food choices impact the environment significantly.**  
- 💡 **Making small, data-driven decisions can help reduce climate impact.**  
""")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------- 🚀 Continue to App -------------------- #
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🚀 Ready to Explore?")
st.write("Click below to continue to the full app experience.")

# ✅ "Continue to App" Button (Navigates to `app.py`)
if st.button("➡️ Continue to App"):
    st.switch_page("app.py")

st.markdown('</div>', unsafe_allow_html=True)
