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
    The future of skincare likely involves hyper-personalized plans analyzing diet, sleep, and stress using advanced technology to identify root causes and tailor treatments for optimal skin health.

    This approach moves beyond basic advice, employing AI and deep learning to understand individual biological and lifestyle factors, leading to customized product recommendations and routines that integrate overall wellness with dermatological care.

    ### Understanding the "Why"
    - **Holistic Approach**: Your skin is a reflection of your internal health, so factors like diet, sleep, and stress significantly impact its condition.
    - **Beyond Surface-Level**: Addressing the root cause of skin issues (e.g., a breakout from stress or poor sleep) is more effective than just treating the symptom.
    - **Technology-Driven**: AI, deep learning, and wearable tech can collect and analyze data to create truly personalized insights, which were previously unavailable.

    ### Key Components of a Hyper-Personalized System
    - **Diet Analysis**: AI-driven analysis of your dietary habits to identify triggers or deficiencies that affect skin health.
    - **Sleep Tracking**: Monitoring sleep patterns to understand its quality and duration, recognizing its crucial role in skin repair and rejuvenation.
    - **Stress Assessment**: Tracking stress levels through biometric data or user input to understand their impact on inflammation, hormonal balance, and skin barrier function.
    - **Integrated AI & Deep Learning**: Algorithms process the collected data to provide actionable insights and recommend specific skincare products, dietary adjustments, stress management techniques, and even tailored routines.

    ### How it Will Work in Practice
    - **Data Collection**: Users might wear biosensors, connect with their smart devices, or provide input through sophisticated surveys about their lifestyle and diet.
    - **AI Analysis**: AI models will process this data to correlate lifestyle habits (diet, sleep, stress) with specific skin concerns and overall skin health.
    - **Personalized Plan**: The system will generate a customized skincare plan that may include:
        - Dietary recommendations: to address nutritional deficiencies or sensitivities.
        - Sleep hygiene tips: to improve rest and recovery.
        - Stress management techniques: such as mindfulness or yoga to calm the body and mind.
        - Customized product suggestions: tailored to your skin's immediate needs.
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
    st.write("Follow these routines for healthy skin:")

    st.subheader("Morning Routine")
    morning_steps = [
        "Morning Cleanse: Gently wash your face to remove impurities that have accumulated overnight.",
        "Tone: Apply an alcohol-free toner to rebalance and rehydrate your skin.",
        "Serum: Apply a targeted serum, such as a Vitamin C serum, to brighten skin and repair sun damage.",
        "Moisturize: Apply a moisturizer to keep your skin soft.",
        "Sunscreen: Apply broad-spectrum SPF 30 or higher to protect against sun damage."
    ]

    st.subheader("Night Routine")
    night_steps = [
        "Remove Makeup: Thoroughly remove all makeup and impurities with a gentle remover.",
        "Cleanse & Tone: Use a gentle cleanser and alcohol-free toner to balance your skin.",
        "Serum: Apply a serum like hyaluronic acid or retinoid for deep treatment.",
        "Eye Cream: Gently apply a lightweight eye cream to address dark circles or puffiness.",
        "Night Cream/Mask: Finish with a nourishing night cream or sleeping mask to lock in moisture."
    ]

    st.subheader("Foods to Include for Healthy Skin")
    food_steps = [
        "Berries, Citrus Fruits, Oranges - Vitamin C & antioxidants",
        "Avocados, Sweet Potatoes - Healthy fats & vitamins",
        "Leafy Greens - Spinach, Kale for vitamins A, C, E",
        "Tomatoes, Carrots - Antioxidants for skin health",
        "Fatty Fish, Nuts, Seeds - Omega-3s for hydration",
        "Avocado & Olive Oil - Healthy fats for skin elasticity",
        "Whole Grains, Legumes - Nutrients & less inflammation",
        "Water & Green Tea - Hydration & antioxidants"
    ]

    all_steps = morning_steps + night_steps + food_steps

    st.write("Mark Yes if followed, No if not followed:")
    routine_score = 0
    for step in all_steps:
        ans = st.radio(step, ["Yes", "No"], key=step)
        if ans == "Yes":
            routine_score += 5
        else:
            routine_score -= 5

    if st.button("Check Routine Score"):
        st.write("Your Routine Score:", routine_score)
        st.session_state.points += max(routine_score, 0)
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
