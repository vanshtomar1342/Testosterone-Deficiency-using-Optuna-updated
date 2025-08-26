import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("best_gradient_boosting_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Testosterone Deficiency Prediction")

st.markdown("""
<div style="background-color:tomato;padding:10px;margin-bottom:10px;">
<h2 style="color:white;text-align:center;">Testosterone Deficiency Prediction ML App</h2>
</div>
""", unsafe_allow_html=True)

# Collect user input
Age = st.slider('How old are you?', 45, 85, 60)
TG = st.text_input('Triglycerides (mg/dl)')
AC = st.text_input('Waist Circumference (cm)')
HDL = st.text_input('High-Density Lipoprotein levels (mg/dl)')
HT = st.toggle('Do you have Hypertension?')
DM = st.toggle('Do you have Diabetes?')

if st.button("Testosterone Deficiency Test Result"):
    try:
        # Prepare input for prediction
        input_data = np.array([
            Age,
            int(DM),
            float(TG),
            int(HT),
            float(HDL),
            float(AC)
        ]).reshape(1, -1)

        # Make prediction
        output = model.predict(input_data)[0]

        if output == 1:
            st.success("The person does not have Testosterone Deficiency (Level >= 300 ng/dl)")
        else:
            st.error("The person has Testosterone Deficiency (Level <300 ng/dl)")
    except Exception as e:
        st.error(f"Error in prediction: {e}")

        