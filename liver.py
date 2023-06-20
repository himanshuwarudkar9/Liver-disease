import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler




def main():
 model = pickle.load(open('Trained_model.pkl', 'rb'))   
    st.title("Liver Disease Prediction")

    age = st.slider("Age", 0, 100, 25)
    gender = st.selectbox("Gender", ["Male", "Female"])
    total_bilirubin = st.number_input("Total Bilirubin")
    direct_bilirubin = st.number_input("Direct Bilirubin")
    alkaline_phosphotase = st.number_input("Alkaline Phosphotase")
    alamine_aminotransferase = st.number_input("Alamine Aminotransferase")
    aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase")
    total_proteins = st.number_input("Total Proteins")
    albumin = st.number_input("Albumin")
    albumin_globulin_ratio = st.number_input("Albumin and Globulin Ratio")
    
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
