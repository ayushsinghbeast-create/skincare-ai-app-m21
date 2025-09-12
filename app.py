import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------- Session States -----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "points" not in st.session_state:
    st.session_state.points = 0

# ----------------- Login/Register -----------------
def login_page():
    st.title("Login / Register")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if user and pwd:
            st.session_state.logged_in = True
            st.success("Login Successful! Use sidebar to navigate features.")
        else:
            st.error("Please enter both username & password")

# ----------------- Skincare Pro Analyzer -----------------
def skincare_analyzer():
    st.title("Skincare Pro Analyzer")
    st.write("Enter Your Health & Lifestyle Details")

    # Image Upload
    img = st.file_uploader("Upload a Selfie (Optional)", type=["jpg","png","jpeg"])

    sleep = st.slider("Sleep Hours", 0, 12, 7)
    water = st.slider("Water Intake (Litres/day)", 0, 5, 2)
    stress = st.slider("Stress Level (1-10)", 1, 10, 5)
    diet = st.slider("Diet Quality (1-10)", 1, 10, 6)
    exercise = st.slider("Exercise Frequency (days/week)", 0, 7, 3)
    screen = st.slider("Screen Time (hours/day)", 0, 12, 6)
    pollution = st.slider("Pollution Exposure (1-10)", 1, 10, 5)
    skin_type = st.selectbox("Skin Type", ["Oily", "Dry", "Normal", "Combination"])

    if st.button("Analyze"):
        score = (sleep + (water*2) + diet + exercise - stress - (screen/2) - pollution) + 20
        future_score = score + 5

        st.subheader("Skin Health Score")
        st.write("Current Score:", round(score, 1))
        st.write("Future Score:", round(future_score, 1))

        st.subheader("Recommendations")
        st.write("- Drink 2-3 liters water daily")
        st.write("- Maintain 7-8 hours of sleep")
        st.write("- Reduce stress via meditation")
        st.write("- Use sunscreen to reduce pollution effects")

        st.subheader("Product Suggestions")
        st.markdown("[Moisturizer - Amazon](https://amazon.in)")
        st.markdown("[Sunscreen - Amazon](https://amazon.in)")

        st.subheader("Skin Progress Over Time")
        fig, ax = plt.subplots()
        ax.plot(["Current", "Future"], [score, future_score], marker="o")
        ax.set_title("Skin Health Progress")
        st.pyplot(fig)

        st.session_state.points += 10
        st.success(f"You earned 10 points! Total Points: {st.session_state.points}")

# ----------------- Daily Skincare Tips -----------------
def daily_tips():
    st.title("Daily Skincare Tips")
    tips = [
        "Cleanse daily", "Moisturize regularly", "Use sunscreen daily", "Exfoliate wisely",
        "Use eye cream", "Stay hydrated", "Eat a balanced diet", "Get enough sleep",
        "Manage stress", "Exercise regularly", "Avoid harsh scrubbing", "Choose appropriate products",
        "Clean your bedding", "Clean makeup applicators", "Check your skin", "Consult a dermatologist",
        "Consider humidity", "Don't neglect your neck", "Don't smoke", "Use serums like Vitamin C"
    ]
    for t in tips:
        st.write("✅", t)
    st.session_state.points += 5
    st.success(f"5 Points Earned! Total: {st.session_state.points}")

# ----------------- AI Skincare Chatbot -----------------
def ai_chatbot():
    st.title("AI Skincare Chatbot")
    questions = {
        "How to reduce acne?": "Use salicylic acid & stay hydrated.",
        "Best sunscreen type?": "Broad spectrum SPF 30 or higher.",
        "How to avoid dry skin?": "Moisturize twice a day & avoid hot water.",
        "Does diet affect skin?": "Yes, eat fruits, veggies & proteins.",
        "Best night routine?": "Cleanse, serum, moisturizer & eye cream.",
        "How much water to drink?": "3-4 liters daily.",
        "Stress effect on skin?": "Stress can cause acne & dullness.",
        "Anti-aging tips?": "Use retinol & sunscreen daily.",
        "How to remove dark spots?": "Vitamin C serums help.",
        "Best cleanser type?": "Gentle, sulfate-free cleansers."
    }
    q = st.selectbox("Select a Question", list(questions.keys()))
    if st.button("Get Answer"):
        st.write("💡", questions[q])
        st.session_state.points += 5

# ----------------- AR Try-On -----------------
def ar_tryon():
    st.title("AR Try-On")
    st.info("AR Try-On feature coming soon!")

# ----------------- Voice Assistant -----------------
def voice_assistant():
    st.title("Voice Assistant")
    st.info("Voice Assistant feature coming soon!")

# ----------------- Skin Prediction AI -----------------
def skin_prediction():
    st.title("Skin Prediction AI")
    st.info("Skin prediction feature coming soon!")

# ----------------- Gamification -----------------
def gamification():
    st.title("Gamification - Earn Points")
    st.write("Points for using features:")
    st.write("Skincare Analyzer: 10 Points")
    st.write("Daily Tips: 5 Points")
    st.write("Chatbot Q&A: 5 Points")
    st.success(f"Your Total Points: {st.session_state.points}")

# ----------------- Hyper Personalized Advice -----------------
def hyper_advice():
    st.title("Hyper-Personalized Skincare Advice")
    st.write("""
    The future of skincare involves hyper-personalized plans analyzing diet, sleep,
    and stress using AI & deep learning for customized recommendations.
    """)

# ----------------- 25 Skincare Tips -----------------
def skincare_25_tips():
    st.title("25 Skincare Tips")
    st.write("""
    - Cleanse Properly
    - Exfoliate Regularly
    - Moisturize Daily
    - Use Sunscreen
    - Remove Makeup Before Sleeping
    - Eat Healthy Diet
    - Stay Hydrated
    - Prioritize Sleep
    - Reduce Stress
    - Avoid Smoking
    - Know Your Skin Type
    - Use Gentle Products
    - Vitamin C Serums
    - Retinol for Anti-aging
    - Pollution Protection
    - Be Gentle When Washing
    - Pat Dry Gently
    - Don't Pop Pimples
    - Care for Body Skin
    - Use Toner
    - 7-Skin Method
    - Double Cleanse at Night
    - Topical Treatments
    - Health Screenings
    - Consult Dermatologist
    """)

# ----------------- Daily Routine AI Checker -----------------
def daily_routine_checker():
    st.title("Daily Routine AI Checker")
    st.write("Follow your routine → Earn Points if completed!")

    routine = {
        "Morning Cleanse": st.checkbox("Morning Cleanse"),
        "Moisturize": st.checkbox("Moisturize"),
        "Sunscreen": st.checkbox("Sunscreen"),
        "Night Serum": st.checkbox("Night Serum"),
        "Sleep 8 hrs": st.checkbox("Sleep 8 hrs")
    }

    if st.button("Check Routine"):
        score = sum([5 if v else -5 for v in routine.values()])
        st.write("Routine Score:", score)
        st.session_state.points += max(score, 0)
        st.success(f"Points Updated! Total: {st.session_state.points}")

# ----------------- Sidebar Navigation -----------------
if not st.session_state.logged_in:
    login_page()
else:
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Go to", [
        "Skincare Pro Analyzer",
        "Daily Skincare Tips",
        "AI Skincare Chatbot",
        "AR Try-On",
        "Voice Assistant",
        "Skin Prediction AI",
        "Gamification",
        "Hyper-Personalized Advice",
        "25 Skincare Tips",
        "Daily Routine AI Checker"
    ])

    if menu == "Skincare Pro Analyzer":
        skincare_analyzer()
    elif menu == "Daily Skincare Tips":
        daily_tips()
    elif menu == "AI Skincare Chatbot":
        ai_chatbot()
    elif menu == "AR Try-On":
        ar_tryon()
    elif menu == "Voice Assistant":
        voice_assistant()
    elif menu == "Skin Prediction AI":
        skin_prediction()
    elif menu == "Gamification":
        gamification()
    elif menu == "Hyper-Personalized Advice":
        hyper_advice()
    elif menu == "25 Skincare Tips":
        skincare_25_tips()
    elif menu == "Daily Routine AI Checker":
        daily_routine_checker()
