import streamlit as st

# Set the title of the app
st.title("Simple Credit Scoring App")

# Description
st.write("Welcome! This is my first simple Streamlit app.")

# User input: monthly income
income = st.number_input("Monthly Income (Toman):", min_value=0)

# User input: age
age = st.slider("Age:", min_value=18, max_value=100, value=30)

# Button to evaluate credit score
if st.button("Check Credit Score"):
    # Simple scoring formula (normalized)
    score = (income / 1_000_000) * 0.3 + (age / 100) * 0.7

    # Display the calculated score
    st.write(f"Your credit score is: {score:.2f}")

    # Display result based on score
    if score > 0.5:
        st.success("Your credit score is good!")
    else:
        st.error("Your credit score needs further evaluation.")
