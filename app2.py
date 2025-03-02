import streamlit as st
# from PIL import Image
# img = Image.open("streamlit.png")
# st.image(img, width=400)

# btn = st.button("Increment")
# count = 0
# count = st.session_state.count =0


# if "count" not in st.session_state:
#     st.session_state.count =0
# if btn:
#     st.session_state.count +=1
#     st.write(btn)
#     st.write(f"button clicked  {st.session_state.count} time")
# else :
#     st.write(f"button not clicked {count} time")

#chat_input = st.chat_input("Enter your prompt")
#if chat_input:
  #  st.chat_message("user").write(chat_input)
 #   st.chat_message("assistant").write("how can i help you today?")
#    st.write(chat_input)

import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter your height (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

bmi = weight / ((height / 100) ** 2)

st.write(f"Your BMI is {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("- Underweight: BMI less than 18.5")
st.write("- Normal weight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obesity: BMI 30 or greater")


