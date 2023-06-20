import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler

model = pickle.load(open('Trained_model.pkl', 'rb'))


def main():   
    st.title("Liver Disease Prediction")

    
    age = st.number_input("Age", min_value=0, step=1)
    gender = st.radio("Gender", ['Male', 'Female'])
    total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, step=0.1)
    direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, step=0.1)
    alkaline_phosphotase = st.number_input("Alkaline Phosphotase", min_value=0, step=1)
    alamine_aminotransferase = st.number_input("Alamine Aminotransferase", min_value=0, step=1)
    aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase", min_value=0, step=1)
    total_proteins = st.number_input("Total Proteins", min_value=0.0, step=0.1)
    albumin = st.number_input("Albumin", min_value=0.0, step=0.1)
    albumin_and_globulin_ratio = st.number_input("Albumin and Globulin Ratio", min_value=0.0, step=0.1)
    
    if st.button("Predict"):    
        values = ([[age, 1 if gender == "Male" else 0, total_bilirubin, direct_bilirubin, alkaline_phosphotase,
                            alamine_aminotransferase, aspartate_aminotransferase, total_proteins, albumin,
                            albumin_globulin_ratio]])
        prediction = model.predict(values)

    if prediction[0]==1.0:
          liver = "You have Liver Disease. 😟"
    else:
          liver = "You don't have Liver Disease. 😃"

    st.success(liver)


if __name__ == "__main__":
    main()
