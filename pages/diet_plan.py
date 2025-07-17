import streamlit as st
from utils.chatbot import generate_diet_plan

st.set_page_config(page_title="🌿 Personalized Sustainable Diet Plan", page_icon="🥗")

# ✅ Custom CSS to Apply a Green-Themed Background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E9F5E1;  /* Light green for an eco-friendly feel */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🥗 GreenBites: Eco-Friendly Personalized Diet Plan")
st.write("Enter your details below to get a **customized diet plan** while minimizing environmental impact. 🌱")

# -------------------- 🌍 User Inputs -------------------- #
st.subheader("🌱 Tell Us About You")

age = st.number_input("Enter your age:", min_value=10, max_value=100, step=1)

# ✅ Weight Unit Selection (Kg or Lbs)
weight_unit = st.radio("Select your weight unit:", ["kg", "lbs"])

weight = st.number_input(f"Enter your weight ({weight_unit}):", min_value=30.0, max_value=500.0, step=0.1)

# ✅ Convert to kg if user enters weight in lbs
if weight_unit == "lbs":
    weight_in_kg = round(weight * 0.453592, 2)  # Convert lbs to kg
else:
    weight_in_kg = weight  # Keep as kg if kg was selected

goal = st.selectbox("Select your goal:", ["Weight Loss", "Muscle Gain", "Maintain Weight"])
diet_preference = st.selectbox("Select your diet preference:", ["Vegetarian", "Vegan", "Non-Vegetarian", "Keto", "Mediterranean"])

# -------------------- 🍽️ Generate Diet Plan Button -------------------- #
if st.button("🌍 Generate My Sustainable Diet Plan"):
    if age and weight:
        with st.spinner("Crafting your sustainable meal plan..."):
            diet_plan = generate_diet_plan(age, weight_in_kg, goal, diet_preference)  # ✅ Pass converted weight
        st.subheader("🌱 Your Sustainable Diet Plan:")
        st.write(diet_plan)
    else:
        st.error("Please enter valid age and weight.")

st.page_link("app.py", label="🏠 Back to Home")
