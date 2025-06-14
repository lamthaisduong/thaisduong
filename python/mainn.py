import streamlit as st

st.title("🔐 Đăng nhập")

username = st.text_input("Tên đăng nhập")
password = st.text_input("Mật khẩu", type="password")

if st.button("Đăng nhập"):
    if username == "admin" and password == "123456":
        st.success("Đăng nhập thành công! Chào mừng, admin.")
    else:
        st.error("Tên đăng nhập hoặc mật khẩu không đúng.")
