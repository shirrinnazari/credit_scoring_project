import streamlit as st

st.title("Credit Scoring Simple App")

st.write("سلام! این اولین اپ ساده استریم‌لیت من است.")

income = st.number_input("درآمد ماهانه (تومان):", min_value=0)
age = st.slider("سن:", 18, 100, 30)

if st.button("بررسی اعتبار"):
    score = (income / 1000000) * 0.3 + (age / 100) * 0.7
    st.write(f"امتیاز اعتبار شما: {score:.2f}")

    if score > 0.5:
        st.success("اعتبار شما خوب است!")
    else:
        st.error("اعتبار شما نیاز به بررسی بیشتر دارد.")
