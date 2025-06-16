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
    background: #222;
    border-radius: 18px;
    box-shadow: 0 4px 24px #0006;
    padding: 2rem 1.5rem 1.5rem 1.5rem;
    margin: 2rem auto;
    max-width: 420px;
}
.slot-symbol {
    font-size: 3.5rem;
    margin: 0.5rem 1.2rem;
    filter: drop-shadow(0 2px 8px #fff8);
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
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="slot-box">', unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center; color:#ff0084; letter-spacing:2px;'>🎰 666 Slot</h1>", unsafe_allow_html=True)

# --- Biểu tượng slot ---
SYMBOLS = ["🍒", "🍋", "🔔", "🍀", "💎", "7️⃣", "⭐", "🍉", "🍇"]

# --- Khởi tạo số dư ---
if "balance" not in st.session_state:
    st.session_state.balance = 1000
if "slots" not in st.session_state:
    st.session_state.slots = [random.choice(SYMBOLS) for _ in range(3)]
if "spinning" not in st.session_state:
    st.session_state.spinning = False
if "last_result" not in st.session_state:
    st.session_state.last_result = ""

# --- Chọn mức cược ---
st.write(f"Số dư: **{st.session_state.balance}** 💰")
bet = st.number_input("Chọn mức cược", min_value=10, max_value=st.session_state.balance, value=10, step=10)

# --- Nút quay ---
spin = st.button("🎲 Quay Nổ Hũ", use_container_width=True)

# --- Quay slot ---
def spin_slots():
    for _ in range(15):
        st.session_state.slots = [random.choice(SYMBOLS) for _ in range(3)]
        slot_cols = st.columns(3)
        for i in range(3):
            slot_cols[i].markdown(f"<div class='slot-symbol'>{st.session_state.slots[i]}</div>", unsafe_allow_html=True)
        time.sleep(0.08)
    # Kết quả cuối cùng
    st.session_state.slots = [random.choice(SYMBOLS) for _ in range(3)]

# --- Xử lý quay ---
if spin and st.session_state.balance >= bet:
    st.session_state.spinning = True
    st.session_state.balance -= bet
    spin_slots()
    slots = st.session_state.slots
    # Luật thắng
    if slots[0] == slots[1] == slots[2]:
        # Nổ hũ lớn với 7️⃣
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
    st.session_state.spinning = False

# --- Hiển thị slot ---
slot_cols = st.columns(3)
for i in range(3):
    slot_cols[i].markdown(f"<div class='slot-symbol'>{st.session_state.slots[i]}</div>", unsafe_allow_html=True)

# --- Hiển thị kết quả ---
if st.session_state.last_result:
    st.markdown(st.session_state.last_result, unsafe_allow_html=True)

# --- Nạp tiền ---
if st.button("Nạp thêm 1000 💰"):
    st.session_state.balance += 1000
    st.success("Đã nạp thêm 1000 💰!")

st.markdown('</div>', unsafe_allow_html=True)
st.info("Chơi giải trí, không dùng cho mục đích cá cược thực tế.")
