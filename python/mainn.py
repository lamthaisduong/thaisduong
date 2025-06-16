import streamlit as st
import random
import time

st.set_page_config(page_title="666 Slot", page_icon="🎰")

# --- CSS cho nền và hiệu ứng ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(120deg, #ffecd2 0%, #fcb69f 100%);
    background-size: 200% 200%;
    animation: gradientBG 10s ease-in-out infinite;
    min-height: 100vh;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
.slot-box {
    background: rgba(34,34,34,0.95);
    border-radius: 18px;
    box-shadow: 0 4px 24px #0006;
    padding: 2.5rem 1.5rem 2rem 1.5rem;
    margin: 2.5rem auto;
    max-width: 440px;
}
.slot-symbol {
    font-size: 3.5rem;
    margin: 0.5rem 1.2rem;
    filter: drop-shadow(0 2px 8px #fff8);
    text-align: center;
}
.big-win {
    color: #ffe600;
    font-size: 2.2rem;
    text-shadow: 0 2px 16px #ff0084, 0 0 8px #fff;
    text-align: center;
    margin-top: 1.2rem;
    margin-bottom: 1.2rem;
    font-weight: bold;
    letter-spacing: 2px;
}
input, button, .stNumberInput, .stButton>button {
    font-size: 1.1rem !important;
}
</style>
""", unsafe_allow_html=True)

# --- Biểu tượng slot ---
SYMBOLS = ["🍒", "🍋", "🔔", "🍀", "💎", "7️⃣", "⭐", "🍉", "🍇"]

# --- Khởi tạo session state ---
if "users" not in st.session_state:
    st.session_state.users = {"admin": "123456"}
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "balance" not in st.session_state:
    st.session_state.balance = 1000
if "slots" not in st.session_state:
    st.session_state.slots = [random.choice(SYMBOLS) for _ in range(3)]
if "last_result" not in st.session_state:
    st.session_state.last_result = ""
if "page" not in st.session_state:
    st.session_state.page = "login"

def register():
    st.markdown('<div class="slot-box">', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#ff0084;'>Đăng ký tài khoản</h2>", unsafe_allow_html=True)
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
    st.markdown('<div class="slot-box">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color:#ff0084;'>🎰 666 Slot</h1>", unsafe_allow_html=True)
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")
    if st.button("Đăng nhập"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Đăng nhập thành công!")
            st.session_state.page = "game"
        else:
            st.error("Sai tên đăng nhập hoặc mật khẩu.")
    if st.button("Đăng ký tài khoản mới"):
        st.session_state.page = "register"
    st.markdown('</div>', unsafe_allow_html=True)

def logout():
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.balance = 1000
        st.session_state.last_result = ""
        st.session_state.page = "login"
        st.success("Đã đăng xuất.")

def slot_game():
    st.markdown('<div class="slot-box">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color:#ff0084;'>🎰 666 Slot</h1>", unsafe_allow_html=True)
    st.write(f"Xin chào, **{st.session_state.username}**")
    st.write(f"Số dư: **{st.session_state.balance}** 💰")
    logout()

    # Kiểm tra số dư tối thiểu
    if st.session_state.balance < 10:
        st.warning("Bạn cần nạp thêm tiền để chơi! (Tối thiểu 10 💰)")
        if st.button("Nạp thêm 1000 💰"):
            st.session_state.balance += 1000
            st.success("Đã nạp thêm 1000 💰!")
        st.markdown('</div>', unsafe_allow_html=True)
        return

    # Chọn mức cược
    bet = st.number_input(
        "Chọn mức cược",
        min_value=10,
        max_value=st.session_state.balance,
        value=min(10, st.session_state.balance),
        step=10
    )

    spin = st.button("🎲 Quay Nổ Hũ", use_container_width=True)

    def spin_slots():
        for _ in range(15):
            st.session_state.slots = [random.choice(SYMBOLS) for _ in range(3)]
            slot_cols = st.columns(3)
            for i in range(3):
                slot_cols[i].markdown(f"<div class='slot-symbol'>{st.session_state.slots[i]}</div>", unsafe_allow_html=True)
            time.sleep(0.08)
        st.session_state.slots = [random.choice(SYMBOLS) for _ in range(3)]

    # Xử lý quay
    if spin and st.session_state.balance >= bet:
        st.session_state.balance -= bet
        spin_slots()
        slots = st.session_state.slots
        # Luật thắng
        if slots[0] == slots[1] == slots[2]:
            if slots[0] == "7️⃣":
                win = bet * 50
                st.session_state.balance += win
                st.session_state.last_result = f"<div class='big-win'>💥 JACKPOT! 7️⃣7️⃣7️⃣ - Thắng {win} 💰</div>"
            else:
                win = bet * 10
                st.session_state.balance += win
                st.session_state.last_result = f"<div class='big-win'>🎉 Nổ hũ! {slots[0]*3} - Thắng {win} 💰</div>"
        elif slots[0] == slots[1] or slots[1] == slots[2] or slots[0] == slots[2]:
            win = bet * 2
            st.session_state.balance += win
            st.session_state.last_result = f"<div class='big-win'>✨ Trúng nhỏ! Thắng {win} 💰</div>"
        else:
            st.session_state.last_result = "<div class='big-win' style='color:#fff;'>Chúc may mắn lần sau!</div>"

    # Hiển thị slot
    slot_cols = st.columns(3)
    for i in range(3):
        slot_cols[i].markdown(f"<div class='slot-symbol'>{st.session_state.slots[i]}</div>", unsafe_allow_html=True)

    # Hiển thị kết quả
    if st.session_state.last_result:
        st.markdown(st.session_state.last_result, unsafe_allow_html=True)

    # Nạp tiền
    if st.button("Nạp thêm 1000 💰"):
        st.session_state.balance += 1000
        st.success("Đã nạp thêm 1000 💰!")

    st.markdown('</div>', unsafe_allow_html=True)
    st.info("Chơi giải trí, không dùng cho mục đích cá cược thực tế.")

# --- ĐIỀU HƯỚNG ---
if not st.session_state.logged_in:
    if st.session_state.page == "login":
        login()
    else:
        register()
else:
    slot_game()
