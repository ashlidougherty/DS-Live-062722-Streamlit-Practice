import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

st.write('# Adoption Prediction')

st.write('## Describe new intake')

col_names = ['Color_black','Fixed','Type_Cat','Type_dog','Intake Condition_Not Normal','Female','Young']

color = st.checkbox(label='Is the animal black')
fixed = st.checkbox(label='Is the animal fixed')
condition = st.checkbox(label='Is the animal intake not normal')
female = st.checkbox(label='Is the animal female')
young = st.checkbox(label='Is the animal young')

type = st.radio(label='What is the animal', options = ['Dog','Cat','Other'])

if type == 'Dog':
    dog_type = True
    cat_type = False
elif type == 'Cat':
    dog_type = False
    cat_type = True 
else:
    cat_type=False
    dog_type=False


if st.button(label = "Click to make prediction"):
    input_row = [color, fixed, cat_type,dog_type, condition, female, young]

    input = pd.DataFrame(dict(zip(col_names,input_row)), index=[0])
    st.write(input)

    loaded_model = pickle.load(open('rf_model.sav', 'rb'))

    prediciton = loaded_model.predict(input)[0]
    
    if prediciton == 1: 
        st.write("this animal is predicted to be adopted")
    else: 
        st.write("this animal is not predicted to be adopted")

