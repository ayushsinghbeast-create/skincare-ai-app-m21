import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ------------------- LOGIN SYSTEM -------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login_page():
    st.title("Login / Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username and password:
            st.session_state.logged_in = True
            st.success("Login Successful!")
        else:
            st.error("Please enter valid credentials")

# ------------------- MAIN APP -------------------
def skincare_pro_analyzer():
    st.title("Skincare Pro Analyzer")

    # Inputs
    st.subheader("Enter Your Health & Lifestyle Details")
    sleep = st.slider("Sleep Hours", 0, 12, 7)
    water = st.slider("Water Intake (Litres/day)", 0, 5, 2)
    stress = st.slider("Stress Level (1-10)", 1, 10, 5)
    diet = st.slider("Diet Quality (1-10)", 1, 10, 6)
    exercise = st.slider("Exercise Frequency (days/week)", 0, 7, 3)
    screen = st.slider("Screen Time (hours/day)", 0, 12, 5)
    pollution = st.slider("Pollution Exposure (1-10)", 1, 10, 5)
    skin_type = st.selectbox("Skin Type", ["Oily", "Dry", "Normal", "Combination"])

    # Calculate Scores
    current_score = (sleep + water + diet + exercise) * 2 - (stress + screen + pollution)
    future_score = current_score + np.random.randint(-5, 5)

    st.subheader("Skin Health Score")
    st.write("Current Score:", current_score)
    st.write("Future Score:", future_score)

    # Recommendations
    st.subheader("Recommendations")
    st.write("• Drink 2-3 liters water daily")
    st.write("• Maintain 7-8 hours of sleep")
    st.write("• Reduce stress via meditation")
    st.write("• Use sunscreen to reduce pollution effects")

    # Product Links
    st.subheader("Product Suggestions (Affiliate Links)")
    st.markdown("[Moisturizer - Amazon](https://amazon.in)")
    st.markdown("[Sunscreen - Amazon](https://amazon.in)")

    # Graph
    st.subheader("Skin Progress Over Time")
    days = np.arange(1, 8)
    scores = current_score + np.random.randint(-3, 3, size=7)
    plt.plot(days, scores, marker='o')
    plt.title("Skin Progress")
    plt.xlabel("Days")
    plt.ylabel("Score")
    st.pyplot(plt)

# ------------------- DAILY ROUTINE AI CHECKER -------------------
def daily_routine_checker():
    st.title("Daily Routine AI Checker")
    st.write("**Morning Routine**")
    st.write("Cleanse → Tone → Serum → Moisturize → Sunscreen")
    st.write("**Night Routine**")
    st.write("Remove Makeup → Cleanse & Tone → Serum → Eye Cream → Night Cream")

    st.write("**Foods for Healthy Skin**")
    st.write("Berries, Citrus Fruits, Avocados, Leafy Greens, Fatty Fish, Nuts, Olive Oil, Green Tea")

    follow = st.radio("Did you follow today's routine?", ["Yes", "No"])
    if follow == "Yes":
        st.success("Great! +5 Points")
    else:
        st.warning("Missed! -5 Points")

# ------------------- HYPER-PERSONALIZED ADVICE -------------------
def hyper_personalized_advice():
    st.title("Hyper-Personalized Skincare Advice")
    st.write("""
    The future of skincare likely involves hyper-personalized plans analyzing diet, sleep, and stress using advanced technology 
    to identify root causes and tailor treatments for optimal skin health.  

    **Understanding the "Why":**  
    - Holistic Approach → Skin reflects internal health.  
    - Beyond Surface-Level → Treat root causes like stress or poor sleep.  
    - Technology-Driven → AI & wearables enable deep analysis.  

    **Key Components:**  
    - Diet Analysis → AI finds deficiencies affecting skin.  
    - Sleep Tracking → Quality & duration insights.  
    - Stress Assessment → Hormone & inflammation impacts.  
    - Deep Learning → Personalized product & lifestyle plans.  

    **How It Works:**  
    1. Data Collection → Wearables, surveys, health inputs.  
    2. AI Analysis → Correlates lifestyle habits with skin issues.  
    3. Personalized Plan → Diet, sleep, stress & product suggestions.  
    """)

# ------------------- AI CHATBOT -------------------
def ai_chatbot():
    st.title("AI Skincare Chatbot")
    st.write("Common Questions:")
    questions = [
        "How to reduce acne?", "Best sunscreen?", "Dry skin solution?",
        "Anti-aging tips?", "Oily skin care routine?"
    ]
    for q in questions:
        if st.button(q):
            st.info(f"Answer for: {q}")

# ------------------- DAILY SKINCARE TIPS -------------------
def daily_tips():
    st.title("Daily Skincare Tips")
    tips = [
        "Wash your face twice a day", "Use moisturizer", "Apply sunscreen daily",
        "Stay hydrated", "Eat healthy food"
    ]
    for t in tips:
        st.success(t)

# ------------------- PLACEHOLDER FEATURES -------------------
def ar_tryon():
    st.title("AR Try-On (Coming Soon)")

def skin_prediction():
    st.title("Skin Prediction AI (Coming Soon)")

def gamification():
    st.title("Gamification")
    st.write("Earn points by following your skincare routine!")

def lifestyle_integration():
    st.title("Lifestyle Integration")
    st.write("Track diet, sleep, stress for better skincare insights!")

# ------------------- SIDEBAR NAVIGATION -------------------
if st.session_state.logged_in:
    st.sidebar.title("Navigation")
    options = [
        "Skincare Pro Analyzer", "Daily Routine AI Checker", "Hyper-Personalized Advice",
        "AI Chatbot", "Daily Skincare Tips", "AR Try-On", "Skin Prediction AI",
        "Gamification", "Lifestyle Integration"
    ]
    choice = st.sidebar.radio("Go to:", options)

    if choice == "Skincare Pro Analyzer":
        skincare_pro_analyzer()
    elif choice == "Daily Routine AI Checker":
        daily_routine_checker()
    elif choice == "Hyper-Personalized Advice":
        hyper_personalized_advice()
    elif choice == "AI Chatbot":
        ai_chatbot()
    elif choice == "Daily Skincare Tips":
        daily_tips()
    elif choice == "AR Try-On":
        ar_tryon()
    elif choice == "Skin Prediction AI":
        skin_prediction()
    elif choice == "Gamification":
        gamification()
    elif choice == "Lifestyle Integration":
        lifestyle_integration()
else:
    login_page()
