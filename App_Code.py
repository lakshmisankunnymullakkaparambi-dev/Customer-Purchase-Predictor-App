# Import Libraries
import pickle
import pandas as pd
import streamlit as st

# Load the dataset (already converted to data.csv) and the saved best model
# -----------------------------------------
df = pd.read_csv("Customer_Purchase_Data.csv")
 
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit Page setup
st.set_page_config(page_title="Customer Purchase Predictor", page_icon="🛒")
st.title("🛒 Customer Purchase Predictor")
st.write("This app uses the best model (already trained in `basic.py`) to predict purchases.")

# Show the data (quick reference)
st.header("Dataset")
st.write(f"Loaded **{df.shape[0]} rows** from `Customer_Purchase_Data.csv`:")
st.dataframe(df)

# Let the user make a prediction
st.header("Try a Prediction")
st.write("Enter details for a new customer:")
 
age_input = st.slider("Age", 18, 70, 30)
gender_input = st.selectbox("Gender", ["Male", "Female"])
income_input = st.number_input("Annual Income ($)", min_value=10000, max_value=200000, value=50000, step=1000)
spending_input = st.slider("Spending Score (0-100)", 0, 100, 50)
marital_input = st.selectbox("Marital Status", ["Single", "Married"])
 
if st.button("Predict"):
    # Convert the inputs into the same format the model was trained on
    gender_num = 0 if gender_input == "Male" else 1
    marital_num = 0 if marital_input == "Single" else 1

    new_customer = pd.DataFrame({
        "Age": [age_input],
        "Gender": [gender_num],
        "AnnualIncome": [income_input],
        "SpendingScore": [spending_input],
        "MaritalStatus": [marital_num],
    })
 
    result = model.predict(new_customer)[0]
 
    if result == 1:
        st.markdown('<div class="result-box buy">✅ This customer is likely to PURCHASE.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-box no-buy">❌ This customer is UNLIKELY to purchase.</div>', unsafe_allow_html=True


        )
