{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7aeb75e-5d80-45de-9977-9a745c99735c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import pickle\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "\n",
    "model = pickle.load(open('Trained_model.pkl', 'rb'))\n",
    "v1 = pickle.load(open('minmax.pkl', 'rb'))\n",
    "\n",
    "def main():\n",
    "    st.title(\"Liver Disease Prediction\")\n",
    "\n",
    "    age = st.slider(\"Age\", 0, 100, 25)\n",
    "    gender = st.selectbox(\"Gender\", [\"Male\", \"Female\"])\n",
    "    total_bilirubin = st.number_input(\"Total Bilirubin\")\n",
    "    direct_bilirubin = st.number_input(\"Direct Bilirubin\")\n",
    "    alkaline_phosphotase = st.number_input(\"Alkaline Phosphotase\")\n",
    "    alamine_aminotransferase = st.number_input(\"Alamine Aminotransferase\")\n",
    "    aspartate_aminotransferase = st.number_input(\"Aspartate Aminotransferase\")\n",
    "    total_proteins = st.number_input(\"Total Proteins\")\n",
    "    albumin = st.number_input(\"Albumin\")\n",
    "    albumin_globulin_ratio = st.number_input(\"Albumin and Globulin Ratio\")\n",
    "\n",
    "    values = v1.transform([[age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase,\n",
    "                            alamine_aminotransferase, aspartate_aminotransferase, total_proteins, albumin,\n",
    "                            albumin_globulin_ratio]])\n",
    "\n",
    "    prediction = model.predict(values)\n",
    "\n",
    "    if prediction[0]==1.0:\n",
    "          liver = \"You have Liver Disease. 😟\"\n",
    "        else:\n",
    "          liver = \"You don't have Liver Disease. 😃\"\n",
    "\n",
    "        st.success(liver)\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
