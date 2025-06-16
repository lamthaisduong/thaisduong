import streamlit as st
import random
import time

st.set_page_config(page_title="666 Slot", page_icon="🎰")

# CSS cho hiệu ứng NỔ HŨ rực rỡ
st.markdown("""
<style>
.slot-frame {
    background: linear-gradient(135deg, #ffe259 0%, #ffa751 100%);
    border-radius: 18px;
    box-shadow: 0 4px 32px #ffb30088;
    padding: 1.5rem 1.2rem 1.2rem 1.2rem;
    margin: 2.5rem auto;
    max-width: 370px;
    min-width: 260px;
    border: 4px solid #fff176;
}
.slot-symbol {
    font-size: 2.7rem;
    margin: 0.3rem 0.7rem;
    filter: drop-shadow(0 2px 8px #fff8);
    text-align: center;
}
.jackpot-anim {
    font-size: 2.2rem;
    font-weight: bold;
    color: #fff700;
    background: linear-gradient(90deg,#fff700,#ff9800,#fff700,#ff9800,#fff700);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: jackpot-blink 0.18s alternate infinite, jackpot-move 2s linear infinite;
    text-align: center;
    margin: 1.2rem 0 0.7rem 0;
    letter-spacing: 3px;
    text-shadow: 0 0 16px #fff, 0 0 32px #ffd600, 0 0 8px #ff9800;
    border-radius: 12px;
}
@keyframes jackpot-blink {
    0% { text-shadow: 0 0 16px #fff, 0 0 32px #ffd600, 0 0 8px #ff9800;}
    100% { text-shadow: 0 0 32px #fff, 0 0 64px #ffd600, 0 0 16px #ff9800;}
}
@keyframes jackpot-move {
    0% {background-position: 0% 50%;}
    100% {background-position: 100% 50%;}
}
.star {
    color: #fff700;
    font-size: 2.2rem;
    position: relative;
    top: 0.2rem;
    margin: 0 0.2rem;
    animation: star-blink 0.3s alternate infinite;
}
@keyframes star-blink {
    0% { filter: brightness(1);}
    100% { filter: brightness(2);}
}
.big-win {
    color: #ffe600;
    font-size: 1.3rem;
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

SYMBOLS = ["🍒", "🍋", "🔔", "🍀", "💎", "7️⃣", "⭐", "🍉", "🍇"]

if "balance" not in st.session_state:
    st.session_state.balance = 1000
if "slots" not in st.session_state:
    st.session_state.slots = [random.choice(SYMBOLS) for _ in range(3)]
if "last_result" not in st.session_state:
    st.session_state.last_result = ""
if "jackpot" not in st.session_state:
    st.session_state.jackpot = False

st.markdown('<div class="slot-frame">', unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#ff0084;'>🎰 666 Slot</h3>", unsafe_allow_html=True)
st.write(f"Số dư: **{st.session_state.balance}** 💰")

bet = st.number_input(
    "Cược",
    min_value=10,
    max_value=st.session_state.balance,
    value=min(10, st.session_state.balance),
    step=10,
    key="bet_input"
)

spin = st.button("🎲 Quay", use_container_width=True)

def spin_slots():
    for _ in range(14):
        st.session_state.slots = [random.choice(SYMBOLS) for _ in range(3)]
        slot_cols = st.columns(3)
        for i in range(3):
            slot_cols[i].markdown(f"<div class='slot-symbol'>{st.session_state.slots[i]}</div>", unsafe_allow_html=True)
        time.sleep(0.06)
    st.session_state.slots = [random.choice(SYMBOLS) for _ in range(3)]

if spin and st.session_state.balance >= bet:
    st.session_state.balance -= bet
    st.session_state.jackpot = False
    spin_slots()
    slots = st.session_state.slots
    if slots[0] == slots[1] == slots[2]:
        if slots[0] == "7️⃣":
            win = bet * 50
            st.session_state.balance += win
            st.session_state.jackpot = True
            st.session_state.last_result = (
                "<div class='jackpot-anim'>"
                "<span class='star'>⭐</span>NỔ HŨ!<span class='star'>⭐</span><br>"
                f"💥 JACKPOT 7️⃣7️⃣7️⃣ 💥<br>Thắng {win} 💰"
                "</div>"
            )
        else:
            win = bet * 10
            st.session_state.balance += win
            st.session_state.last_result = f"<div class='big-win'>🎉 Nổ hũ! {slots[0]*3} - Thắng {win} 💰</div>"
    elif slots[0] == slots[1] or slots[1] == slots[2] or slots[0] == slots[2]:
        win = bet * 2
        st.session_state.balance += win
        st.session_state.last_result = f"<div class='big-win'>✨ Trúng nhỏ! Thắng {win} 💰</div>"
    else:
        st.session_state.last_result = "<div style='color:#fff;text-align:center;'>Chúc may mắn lần sau!</div>"

# Hiển thị slot
slot_cols = st.columns(3)
for i in range(3):
    slot_cols[i].markdown(f"<div class='slot-symbol'>{st.session_state.slots[i]}</div>", unsafe_allow_html=True)

# Hiển thị kết quả
if st.session_state.last_result:
    st.markdown(st.session_state.last_result, unsafe_allow_html=True)

if st.button("Nạp thêm 1000 💰"):
    st.session_state.balance += 1000
    st.success("Đã nạp thêm 1000 💰!")

st.markdown('</div>', unsafe_allow_html=True)
st.info("Chơi giải trí, không dùng cho mục đích cá cược thực tế.")
