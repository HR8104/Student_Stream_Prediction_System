import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('final1.pkl','rb'))
print(type(model))

st.title("Career and Stream Recommendation System")
st.header("Input Student Scores")

# Input fields for features
math_score = st.number_input("Math Score", min_value=0, max_value=100, value=50)
science_score = st.number_input("Science Score", min_value=0, max_value=100, value=50)
english_score = st.number_input("English Score", min_value=0, max_value=100, value=50)
social_studies_score = st.number_input("Social Studies Score", min_value=0, max_value=100, value=50)
logical_aptitude = st.number_input("Logical Aptitude", min_value=0, max_value=100, value=50)
verbal_aptitude = st.number_input("Verbal Aptitude", min_value=0, max_value=100, value=50)
quantitative_aptitude = st.number_input("Quantitative Aptitude", min_value=0, max_value=100, value=50)

if st.button("Predict"):
    input_data = [[math_score, science_score, english_score, social_studies_score,logical_aptitude, verbal_aptitude, quantitative_aptitude]]
    pred = model.predict(input_data)
    if pred == -1:
        st.write("you should go with Arts")
    elif pred == 0:
        st.write("you should go with commerce")
    else:
        st.write("you should go with science")



