import streamlit as st
import random

st.title("🎲 Game Tài Xỉu Đơn Giản")

st.write("Chọn số tiền cược và dự đoán kết quả:")

bet = st.number_input("Số tiền cược", min_value=10, max_value=100000, value=100, step=10)
choice = st.radio("Bạn chọn:", ("Tài (11-17)", "Xỉu (4-10)"))

if st.button("Lắc xúc xắc"):
    dice = [random.randint(1, 6) for _ in range(3)]
    total = sum(dice)
    st.write(f"🎲 Kết quả: {dice[0]}, {dice[1]}, {dice[2]} (Tổng: {total})")
    if 4 <= total <= 10:
        result = "Xỉu"
    elif 11 <= total <= 17:
        result = "Tài"
    else:
        result = "Bộ ba đặc biệt (3 hoặc 18)"
    st.write(f"Kết quả: **{result}**")
    if result in choice:
        st.success(f"Bạn thắng! Nhận được {bet*2} VNĐ")
    elif result == "Bộ ba đặc biệt (3 hoặc 18)":
        st.warning("Bộ ba đặc biệt! Nhà cái ăn hết.")
    else:
        st.error("Bạn thua!")

st.info("Đây chỉ là game mô phỏng, không dùng cho mục đích cá cược thực tế.")
