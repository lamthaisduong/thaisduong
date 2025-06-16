import streamlit as st
import random
import time

MIN_BET = 10

if "users" not in st.session_state:
    st.session_state.users = {"admin": "123456"}
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "balance" not in st.session_state:
    st.session_state.balance = 0
if "show_overlay" not in st.session_state:
    st.session_state.show_overlay = False
if "overlay_start_time" not in st.session_state:
    st.session_state.overlay_start_time = 0
if "overlay_dice" not in st.session_state:
    st.session_state.overlay_dice = [1, 1, 1]
if "overlay_text" not in st.session_state:
    st.session_state.overlay_text = ""

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

def register():
    set_animated_background()
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color:#ffe600; letter-spacing:2px; text-shadow:0 2px 12px #00c3ff;'>🎰 BET 888</h1>", unsafe_allow_html=True)
    st.subheader("Đăng ký tài khoản mới")
    new_user = st.text_input("Tên đăng nhập mới")
    new_pass = st.text_input("Mật khẩu mới", type="password")
    confirm_pass = st.text_input("Nhập lại mật khẩu", type="password")
    if st.button("Đăng ký"):
        if not new_user or not new_pass:
            st.error("Vui lòng nhập đầy đủ thông tin.")
        elif new_user in st.session_state.users:
            st.error("Tên đăng nhập đã tồn tại.")
        elif new_pass != confirm_pass:
            st.error("Mật khẩu nhập lại không khớp.")
        else:
            st.session_state.users[new_user] = new_pass
            st.success("Đăng ký thành công! Bạn có thể đăng nhập.")
            st.session_state.page = "login"
    if st.button("Quay lại đăng nhập"):
        st.session_state.page = "login"
    st.markdown('</div>', unsafe_allow_html=True)

def login():
    set_animated_background()
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color:#ffe600; letter-spacing:2px; text-shadow:0 2px 12px #00c3ff;'>🎰 BET 888</h1>", unsafe_allow_html=True)
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")
    if st.button("Đăng nhập"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Đăng nhập thành công!")
        else:
            st.error("Sai tên đăng nhập hoặc mật khẩu.")
    if st.button("Đăng ký tài khoản mới"):
        st.session_state.page = "register"
    st.markdown('</div>', unsafe_allow_html=True)

def logout():
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.session_state.username = ""
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
    st.markdown(f"<h1 style='text-align:center; color:#ffe600; letter-spacing:2px; text-shadow:0 2px 12px #00c3ff;'>🎰 BET 888</h1>", unsafe_allow_html=True)
    st.write(f"Xin chào, **{st.session_state.username}**")
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

    # Xử lý overlay xúc xắc tự động tắt sau 3 giây
    if st.session_state.show_overlay:
        show_dice_overlay(st.session_state.overlay_dice, st.session_state.overlay_text)
        # Nếu đã đủ 3 giây thì tắt overlay và rerun
        if time.time() - st.session_state.overlay_start_time > 3:
            st.session_state.show_overlay = False
            st.experimental_rerun()
        st.stop()

    if roll_btn:
        # Hiệu ứng xúc xắc to phủ màn hình
        for i in range(10):
            dice = [random.randint(1, 6) for _ in range(3)]
            show_dice_overlay(dice, "Đang lắc...")
            time.sleep(0.13)
        dice = [random.randint(1, 6) for _ in range(3)]
        total = sum(dice)
        st.session_state.overlay_dice = dice
        st.session_state.overlay_text = f"Kết quả: Tổng = {total}"
        st.session_state.show_overlay = True
        st.session_state.overlay_start_time = time.time()
        st.experimental_rerun()

    # Nếu không đang overlay thì xử lý kết quả
    if not st.session_state.show_overlay and roll_btn:
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

# Điều hướng giữa đăng nhập và đăng ký
if "page" not in st.session_state:
    st.session_state.page = "login"

if not st.session_state.logged_in:
    if st.session_state.page == "login":
        login()
    else:
        register()
else:
    tai_xiu_game()
