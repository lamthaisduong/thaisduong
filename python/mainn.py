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
if "show_overlay" not in st.session_state:
    st.session_state.show_overlay = False

def set_animated_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(270deg, #0f2027, #2c5364, #00c3ff, #ffff1c, #ff6a00, #ff0084, #33001b, #0f2027);
            background-size: 1600% 1600%;
            animation: gradientBG 30s ease-in-out infinite;
            min-height: 100vh;
        }
        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            25% {background-position: 50% 100%;}
            50% {background-position: 100% 50%;}
            75% {background-position: 50% 0%;}
            100% {background-position: 0% 50%;}
        }
        .main-content {
            background: rgba(20,24,40,0.82);
            border-radius: 22px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.25);
            padding: 2.5rem 2rem 2rem 2rem;
            margin: 2.5rem auto;
            max-width: 500px;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_dice_overlay(dice, text=""):
    st.markdown(
        f"""
        <style>
        .dice-overlay {{
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(0,0,0,0.75);
            z-index: 99999;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}
        .dice-big {{
            font-size: 9rem;
            color: #ffe600;
            text-shadow: 0 4px 32px #000, 0 0 24px #00c3ff, 0 0 48px #ff0084;
            margin-bottom: 2.5rem;
        }}
        .dice-text {{
            font-size: 2.5rem;
            color: #fff;
            text-shadow: 0 2px 8px #000;
        }}
        </style>
        <div class="dice-overlay">
            <div class="dice-big">🎲 {dice[0]}, {dice[1]}, {dice[2]}</div>
            <div class="dice-text">{text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def login():
    set_animated_background()
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color:#ffe600; letter-spacing:2px; text-shadow:0 2px 12px #00c3ff;'>🎰 BET 888</h1>", unsafe_allow_html=True)
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
    st.markdown("<h1 style='text-align:center; color:#ffe600; letter-spacing:2px; text-shadow:0 2px 12px #00c3ff;'>🎰 BET 888</h1>", unsafe_allow_html=True)
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

    result_placeholder = st.empty()

    if roll_btn:
        st.session_state.show_overlay = True
        # Hiệu ứng xúc xắc to phủ màn hình
        for i in range(10):
            dice = [random.randint(1, 6) for _ in range(3)]
            show_dice_overlay(dice, "Đang lắc...")
            time.sleep(0.13)
        dice = [random.randint(1, 6) for _ in range(3)]
        total = sum(dice)
        show_dice_overlay(dice, f"Kết quả: Tổng = {total}")
        time.sleep(1.2)
        st.session_state.show_overlay = False

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
    else:
        st.session_state.show_overlay = False

    logout()
    st.info("Đây chỉ là game mô phỏng, không dùng cho mục đích cá cược thực tế.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Hiển thị overlay nếu đang lắc
    if st.session_state.show_overlay:
        show_dice_overlay([random.randint(1, 6) for _ in range(3)], "Đang lắc...")

if not st.session_state.logged_in:
    login()
else:
    tai_xiu_game()
