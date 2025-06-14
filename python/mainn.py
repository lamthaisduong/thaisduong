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

def set_animated_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(120deg, #e0c3fc 0%, #8ec5fc 100%);
            background-size: 200% 200%;
            animation: gradientBG 10s ease-in-out infinite;
        }
        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        .main-content {
            background: rgba(255,255,255,0.85);
            border-radius: 18px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
            padding: 2.5rem 2rem 2rem 2rem;
            margin: 2rem auto;
            max-width: 480px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def login():
    set_animated_background()
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color:#5f2c82;'>🎰 BET 888</h1>", unsafe_allow_html=True)
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")
    if st.button("Đăng nhập"):
        if username == USER and password == PASS:
            st.session_state.logged_in = True
            st.success("Đăng nhập thành công!")
        else:
            st.error("Sai tên đăng nhập hoặc mật khẩu.")
    st.markdown('</div>', unsafe_allow_html=True)

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
    set_animated_background()
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color:#5f2c82;'>🎰 BET 888</h1>", unsafe_allow_html=True)
    st.write(f"Số dư hiện tại: **{st.session_state.balance} VNĐ**")
    recharge()
    st.markdown("---")
    if st.session_state.balance < MIN_BET:
        st.warning(f"Số dư của bạn nhỏ hơn mức cược tối thiểu ({MIN_BET} VNĐ). Vui lòng nạp thêm tiền để chơi.")
        logout()
        st.markdown('</div>', unsafe_allow_html=True)
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

    def show_dice_center(dice, text=""):
        dice_html = f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div style="font-size: 2.5rem; color:#5f2c82;">🎲 {dice[0]}, {dice[1]}, {dice[2]}</div>
            <div style="margin-top: 8px; color:#5f2c82;">{text}</div>
        </div>
        """
        dice_placeholder.markdown(dice_html, unsafe_allow_html=True)

    if roll_btn:
        for i in range(10):
            dice = [random.randint(1, 6) for _ in range(3)]
            show_dice_center(dice, "Đang lắc...")
            time.sleep(0.15)
        dice = [random.randint(1, 6) for _ in range(3)]
        total = sum(dice)
        show_dice_center(dice, f"Kết quả: Tổng = {total}")

        # Tỉ lệ thắng 20%
        win_chance = random.randint(1, 100)
        if win_chance <= 20:
            # Người chơi thắng
            if choice == "Tài (11-17)":
                result = "Tài"
            else:
                result = "Xỉu"
        else:
            # Người chơi thua
            if choice == "Tài (11-17)":
                result = "Xỉu"
            else:
                result = "Tài"

        result_placeholder.write(f"Kết quả: **{result}**")
        if result in choice:
            st.session_state.balance += bet
            st.success(f"Bạn thắng! Nhận {bet} VNĐ. Số dư: {st.session_state.balance} VNĐ")
        else:
            st.session_state.balance -= bet
            st.error(f"Bạn thua! Mất {bet} VNĐ. Số dư: {st.session_state.balance} VNĐ")
    logout()
    st.info("Đây chỉ là game mô phỏng, không dùng cho mục đích cá cược thực tế.")
    st.markdown('</div>', unsafe_allow_html=True)

if not st.session_state.logged_in:
    login()
else:
    tai_xiu_game()
