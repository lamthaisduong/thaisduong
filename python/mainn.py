import streamlit as st
import random
import time

USER = "admin"
PASS = "123456"
MIN_BET = 10

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "balance" not in st.session_state:
    st.session_state.balance = 0

def login():
    st.title("🔐 Đăng nhập")
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")
    if st.button("Đăng nhập"):
        if username == USER and password == PASS:
            st.session_state.logged_in = True
            st.success("Đăng nhập thành công!")
        else:
            st.error("Sai tên đăng nhập hoặc mật khẩu.")

def logout():
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.session_state.balance = 0
        st.success("Đã đăng xuất.")

def recharge():
    st.subheader("💰 Nạp tiền vào tài khoản")
    amount = st.number_input("Nhập số tiền muốn nạp", min_value=MIN_BET, max_value=1000000, value=100, step=10)
    if st.button("Nạp tiền"):
        st.session_state.balance += amount
        st.success(f"Đã nạp {amount} VNĐ. Số dư hiện tại: {st.session_state.balance} VNĐ")

def tai_xiu_game():
    st.title("🎲 Game Tài Xỉu Đơn Giản")
    st.write(f"Số dư hiện tại: **{st.session_state.balance} VNĐ**")
    recharge()
    st.markdown("---")
    if st.session_state.balance < MIN_BET:
        st.warning(f"Số dư của bạn nhỏ hơn mức cược tối thiểu ({MIN_BET} VNĐ). Vui lòng nạp thêm tiền để chơi.")
        logout()
        return

    st.write("Chọn số tiền cược và dự đoán kết quả:")
    bet = st.number_input(
        "Số tiền cược",
        min_value=MIN_BET,
        max_value=st.session_state.balance,
        value=MIN_BET,
        step=10,
        key="bet_input"
    )
    choice = st.radio("Bạn chọn:", ("Tài (11-17)", "Xỉu (4-10)"))
    roll_btn = st.button("Lắc xúc xắc")

    dice_placeholder = st.empty()
    result_placeholder = st.empty()

    if roll_btn:
        # Hiệu ứng lắc xúc xắc chuyển động
        for i in range(10):
            dice = [random.randint(1, 6) for _ in range(3)]
            dice_placeholder.write(f"🎲 Đang lắc: {dice[0]}, {dice[1]}, {dice[2]}")
            time.sleep(0.15)
        # Kết quả cuối cùng
        dice = [random.randint(1, 6) for _ in range(3)]
        total = sum(dice)
        dice_placeholder.write(f"🎲 Kết quả: {dice[0]}, {dice[1]}, {dice[2]} (Tổng: {total})")
        if 4 <= total <= 10:
            result = "Xỉu"
        elif 11 <= total <= 17:
            result = "Tài"
        else:
            result = "Bộ ba đặc biệt (3 hoặc 18)"
        result_placeholder.write(f"Kết quả: **{result}**")
        if result in choice:
            st.session_state.balance += bet
            st.success(f"Bạn thắng! Nhận {bet} VNĐ. Số dư: {st.session_state.balance} VNĐ")
        elif result == "Bộ ba đặc biệt (3 hoặc 18)":
            st.session_state.balance -= bet
            st.warning(f"Bộ ba đặc biệt! Nhà cái ăn hết. Số dư: {st.session_state.balance} VNĐ")
        else:
            st.session_state.balance -= bet
            st.error(f"Bạn thua! Mất {bet} VNĐ. Số dư: {st.session_state.balance} VNĐ")
    logout()
    st.info("Đây chỉ là game mô phỏng, không dùng cho mục đích cá cược thực tế.")

if not st.session_state.logged_in:
    login()
else:
    tai_xiu_game()
