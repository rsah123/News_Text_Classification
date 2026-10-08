import streamlit as st
import joblib

model = joblib.load("news_classification_model.pkl")

st.title("News Text Classification System")
st.write(
    "Enter a news article below and the model will classify it into "
    "Business, Entertainment, Politics, Sport, or Tech."
)

news_text = st.text_area(
    "Enter News Article",
    height=250
)
if st.button("Classify News"):

    if news_text.strip() == "":
        st.warning("Please enter a news article first.")

    else:
        prediction = model.predict([news_text])[0]

        st.success(
            f"Predicted Category: {prediction.title()}"
        )