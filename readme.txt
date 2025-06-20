# Vaishnavi's Real Estate Price Prediction Dashboard

This is a Streamlit-based interactive dashboard developed by Vaishnavi. It predicts house prices in Bengaluru based on user inputs and provides a basic risk score using machine learning.

---

## 📌 Project Summary

This project uses a trained Random Forest Regression model to estimate the selling price of a house based on:

- Total square feet (`total_sqft`)
- Number of bathrooms (`bath`)
- Number of bedrooms (`BHK`)

Additionally, it calculates a **risk score** based on simple logical conditions to assess whether the listing may be potentially overpriced, underbuilt, or mismatched in utility.

---

## 📁 Project Folder Contains:

- `app.py` – Streamlit dashboard code
- `model.pkl` – Trained Random Forest model saved via pickle
- `Bengaluru_House_Data_Expanded.csv` – Dataset used for training & demo
- `README.txt` – You are reading it!

---

## 🛠️ Technologies Used:

- Python 3
- Streamlit – For creating the dashboard UI
- pandas – For data handling
- scikit-learn – For training the regression model
- pickle – For saving the trained model

---

## ⚙️ How to Run the Project

1. Make sure Python and Streamlit are installed:
   pip install streamlit pandas scikit-learn

2. Place all files (`app.py`, `model.pkl`, `.csv`) in the same folder

3. Open Command Prompt (CMD), navigate to the folder:
   cd path_to_your_folder

4. Run the dashboard:
   streamlit run app.py

The dashboard will automatically open in your browser.

---

## 💡 Features

⚠️ **Note:** The file `model.pkl` is a trained Random Forest model saved in binary format.  
GitHub does not support previewing `.pkl` files directly, but it is included in this repository and can be used to run the Streamlit dashboard.

If you face any issues, you can also [download model.pkl from Google Drive](https://drive.google.com/your-link-here) 🔗

- Predicts house price instantly
- Risk score displayed for quick insights
- Live dataset preview on the dashboard
- Clean UI and intuitive flow
- Built with minimal dependencies

---

## 🧠 Risk Logic Used

- High Risk: sqft < 1000 and bath < BHK
- Medium Risk: Either sqft < 1000 or bath < BHK
- Low Risk: Neither condition met

---

## 👩‍💻 Created by

Vaishnavi  
Bachelor of Computer Applications (BCA) Student  
Passionate about AI, Data Science & User-Centric Tech

---

## 📬 Contact (Optional)

If you're viewing this for evaluation, feel free to reach out for more insights or improvements!
