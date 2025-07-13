import streamlit as st

st.title("Credit Scoring Simple App")

st.write("Hello! This is my first simple Streamlit app.")

income = st.number_input("Monthly Income (Toman):", min_value=0)
age = st.slider("Age:", 18, 100, 30)

if st.button("Check Credit Score"):
    score = (income / 1000000) * 0.3 + (age / 100) * 0.7
    st.write(f"Your credit score is: {score:.2f}")

    if score > 0.5:
        st.success("Your credit score is good!")
    else:
        st.error("Your credit score needs further review.")
