
import streamlit as st
from utils.workout_data import default_ppl
from utils.camera_utils import capture_food_image

st.set_page_config(page_title="Gym PPL Tracker", layout="centered")

st.title("🏋️ Gym Workout & Nutrition Tracker")

# --- User Inputs ---
st.sidebar.header("Customize Your Plan")
training_days = st.sidebar.slider("Training Days / Week", 1, 7, 5)
running_days = st.sidebar.slider("Running Days / Week", 0, 7, 2)
daily_protein_target = st.sidebar.number_input("Protein Target (g)", 50, 250, 120)
daily_calorie_target = st.sidebar.number_input("Calories Target (kcal)", 1200, 4000, 2200)

# --- Workout Plan ---
st.header("🗓️ Your Weekly PPL Workout Plan")

ppl = ['Push', 'Pull', 'Legs']
custom_ppl = {}
for day in ppl:
    exercises = st.text_area(f"{day} Day Exercises (comma-separated)", 
                             value=", ".join(default_ppl.get(day, [])))
    custom_ppl[day] = [ex.strip() for ex in exercises.split(",") if ex.strip()]

st.success("✅ Plan Updated!")

# --- Protein Intake ---
st.header("🍗 Protein Intake Tracker")

protein_today = st.number_input("Enter Protein Intake Today (g)", 0, 300, 0)
calories_today = st.number_input("Enter Calories Intake Today", 0, 5000, 0)

st.metric("Protein Left", f"{max(0, daily_protein_target - protein_today)}g")
st.metric("Calories Left", f"{max(0, daily_calorie_target - calories_today)} kcal")

# --- Food Image Upload ---
st.subheader("📷 Upload or Click Food Image to Estimate Protein")
capture_food_image()

st.caption("🧠 (Note: Currently no ML model used — estimation is manual)")

st.markdown("---")
st.caption("Made with ❤️ by Jimmyy")
