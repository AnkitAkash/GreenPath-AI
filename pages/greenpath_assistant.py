import streamlit as st
from datetime import datetime
from utils.chatbot import get_carbon_emission, generate_sustainability_report
from utils.helpers import get_coordinates, get_travel_distance, autocomplete_address


st.set_page_config(page_title="GreenPath Assistant", page_icon="🚗")

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

st.title("🚗 GreenPath Travel AI Assistant")
st.write("Plan your journey, calculate travel time, and estimate your **carbon footprint**.")

# Store trip data in session state
if "distance_km" not in st.session_state:
    st.session_state.distance_km = None
if "mode_of_transport" not in st.session_state:
    st.session_state.mode_of_transport = None
if "expected_time" not in st.session_state:
    st.session_state.expected_time = None
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# Address Input Fields with Autocompletion
source_input = st.text_input("Enter Source Address")
destination_input = st.text_input("Enter Destination Address")

if source_input:
    suggested_source = autocomplete_address(source_input)
    if suggested_source:
        source_input = suggested_source
        st.text_input("Auto-Completed Source Address", value=source_input, key="source_autofill", disabled=True)

if destination_input:
    suggested_destination = autocomplete_address(destination_input)
    if suggested_destination:
        destination_input = suggested_destination
        st.text_input("Auto-Completed Destination Address", value=destination_input, key="destination_autofill", disabled=True)

# Transport Mode Dropdown
mode_of_transport = st.selectbox("Select Mode of Transport", ["Car", "Bicycle", "Walk", "Public Transport"])

# Calculate Travel Time & Distance
if st.button("Calculate Travel Time & Distance"):
    source_coords = get_coordinates(source_input)
    dest_coords = get_coordinates(destination_input)

    if source_coords and dest_coords:
        distance_km, time_taken = get_travel_distance(source_coords, dest_coords, mode_of_transport)
        if distance_km and time_taken:
            st.session_state.distance_km = distance_km
            st.session_state.mode_of_transport = mode_of_transport
            st.session_state.expected_time = time_taken
            st.success(f"🚗 Estimated Travel Time: {time_taken} minutes")
            st.success(f"📏 Estimated Travel Distance: {distance_km} km")
        else:
            st.error("Could not calculate travel details. Try again.")
    else:
        st.error("Invalid address. Please check again.")

# Start Trip Button
if st.button("Start Trip"):
    st.session_state.start_time = datetime.now()
    st.success("✅ Trip Started! Press 'End Trip' when you reach your destination.")

# End Trip Button & Verification
if st.button("End Trip"):
    if st.session_state.start_time:
        end_time = datetime.now()
        actual_time_taken = (end_time - st.session_state.start_time).total_seconds() / 60
        st.info(f"🕒 Your Actual Travel Time: {round(actual_time_taken, 2)} minutes")

        if st.session_state.expected_time:
            expected_time = st.session_state.expected_time
            mode_margins = {"Walk": 0.3, "Bicycle": 0.2, "Car": 0.25, "Public Transport": 0.3}
            allowed_margin = mode_margins.get(st.session_state.mode_of_transport, 0.2)
            min_time = expected_time * 0.5
            max_time = expected_time * (1 + allowed_margin)

            if min_time <= actual_time_taken <= max_time:
                st.success("✅ Verification Successful! Your travel time was within an expected range. 🌱")
            else:
                st.error("❌ Verification Failed! Your travel time was too different from the expected duration.")
        else:
            st.error("⚠️ No expected time found. Please calculate the trip first.")
    else:
        st.error("⚠️ Please press 'Start Trip' before ending it.")

# AI-Generated Sustainability Report
if st.button("Get AI Sustainability Report"):
    if st.session_state.distance_km:
        report = generate_sustainability_report(st.session_state.distance_km, st.session_state.mode_of_transport)
        st.info(report)
    else:
        st.error("Please calculate a trip first!")

# AI Chat for Climate Education
question = st.text_input("Ask GreenPath about sustainability (e.g., 'How does my trip compare to an EV?')")
if st.button("Ask GreenPath"):
    if question and st.session_state.distance_km:
        ai_response = get_carbon_emission(question, st.session_state.distance_km, st.session_state.mode_of_transport)
        st.success(f"🤖 AI Answer: {ai_response}")
    else:
        st.error("Calculate a trip first before asking AI!")

st.page_link("app.py", label="Back to Home", icon="🏡")

