import streamlit as st
from utils.workout_data import default_ppl
from utils.camera_utils import capture_food_image
import datetime
import json
import os

# --- Configuration ---
st.set_page_config(page_title="Gym PPL Tracker", layout="centered")
DATA_FILE = "data.json"

# --- Load Data ---
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"date": "", "protein": 0, "calories": 0}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# --- Save Data ---
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# --- Reset Daily If Needed ---
def check_and_reset(data):
    today = str(datetime.date.today())
    if data["date"] != today:
        data["date"] = today
        data["protein"] = 0
        data["calories"] = 0
        save_data(data)
    return data

# --- Main App Logic ---
data = load_data()
data = check_and_reset(data)

# --- CSS Styling ---
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 2rem;
        }
        h1, h2, h3 {
            color: #3b3b3b;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            font-size: 16px;
            border-radius: 10px;
        }
        .css-1aumxhk {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("🏋️ Gym Workout & Nutrition Tracker")
st.write(f"📅 Date: **{data['date']}**")

# --- Sidebar Navigation ---
selected = st.sidebar.selectbox(
    "Navigate",
    ["🏠 Home", "💪 Workout Log", "🍽 Nutrition", "📊 Summary"]
)

# --- Sidebar Customization ---
st.sidebar.header("Customize Your Plan")
training_days = st.sidebar.slider("Training Days / Week", 1, 7, 5)
running_days = st.sidebar.slider("Running Days / Week", 0, 7, 2)
daily_protein_target = st.sidebar.number_input("Protein Target (g)", 50, 250, 120)
daily_calorie_target = st.sidebar.number_input("Calories Target (kcal)", 1200, 4000, 2200)

# --- Page Rendering ---
if selected == "🏠 Home":
    st.header("🏠 Welcome to FitTrack")
    st.markdown("Use the sidebar to log workouts, track nutrition, and see your progress.")

elif selected == "💪 Workout Log":
    st.header("🗓️ Your Weekly PPL Workout Plan")
    ppl = ['Push', 'Pull', 'Legs']
    custom_ppl = {}
    for day in ppl:
        exercises = st.text_area(f"{day} Day Exercises (comma-separated)", 
                                 value=", ".join(default_ppl.get(day, [])))
        custom_ppl[day] = [ex.strip() for ex in exercises.split(",") if ex.strip()]
    st.success("✅ Plan Updated!")

elif selected == "🍽 Nutrition":
    st.header("🍗 Protein & Calorie Intake Tracker")

    # Get inputs from user
    protein_input = st.number_input("Enter Protein Intake Today (g)", min_value=0, max_value=300, value=0, step=1)
    calorie_input = st.number_input("Enter Calories Intake Today", min_value=0, max_value=5000, value=0, step=10)

    if st.button("Update Today's Data"):
        data["protein"] += protein_input
        data["calories"] += calorie_input
        save_data(data)
        st.success("✅ Data updated!")

    st.metric("Protein Left", f"{max(0, daily_protein_target - data['protein'])}g")
    st.metric("Calories Left", f"{max(0, daily_calorie_target - data['calories'])} kcal")

    st.subheader("📷 Upload or Click Food Image to Estimate Protein")
    capture_food_image()
    st.caption("🧠 (Note: Currently no ML model used — estimation is manual)")

elif selected == "📊 Summary":
    st.header("📊 Daily Summary")
    st.write(f"**Total Protein Today**: {data['protein']} g")
    st.write(f"**Total Calories Today**: {data['calories']} kcal")
    st.progress(data['protein'] / daily_protein_target)
    st.progress(data['calories'] / daily_calorie_target)

# --- Footer ---
st.markdown("---")
st.caption("Made with ❤️ by Jimmyy")
