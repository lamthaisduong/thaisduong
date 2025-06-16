import streamlit as st
import random
import time

st.set_page_config(page_title="666 Slot", page_icon="🎰")

# CSS cho khung nhỏ gọn và hiệu ứng trúng lớn
st.markdown("""
<style>
.slot-frame {
    background: rgba(34,34,34,0.97);
    border-radius: 18px;
    box-shadow: 0 4px 24px #0008;
    padding: 1.5rem 1.2rem 1.2rem 1.2rem;
    margin: 2.5rem auto;
    max-width: 340px;
    min-width: 260px;
}
.slot-symbol {
    font-size: 2.5rem;
    margin: 0.3rem 0.7rem;
    filter: drop-shadow(0 2px 8px #fff8);
    text-align: center;
}
.big-win-anim {
    color: #ffe600;
    font-size: 1.6rem;
    text-shadow: 0 2px 16px #ff0084, 0 0 8px #fff;
    text-align: center;
    margin-top: 1.2rem;
    margin-bottom: 1.2rem;
    font-weight: bold;
    letter-spacing: 2px;
    animation: blink 0.25s alternate infinite;
}
@keyframes blink {
    0% { opacity: 1;}
    100% { opacity: 0.3;}
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
if "big_win" not in st.session_state:
    st.session_state.big_win = False

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
    for _ in range(12):
        st.session_state.slots = [random.choice(SYMBOLS) for _ in range(3)]
        slot_cols = st.columns(3)
        for i in range(3):
            slot_cols[i].markdown(f"<div class='slot-symbol'>{st.session_state.slots[i]}</div>", unsafe_allow_html=True)
        time.sleep(0.07)
    st.session_state.slots = [random.choice(SYMBOLS) for _ in range(3)]

if spin and st.session_state.balance >= bet:
    st.session_state.balance -= bet
    st.session_state.big_win = False
    spin_slots()
    slots = st.session_state.slots
    if slots[0] == slots[1] == slots[2]:
        if slots[0] == "7️⃣":
            win = bet * 50
            st.session_state.balance += win
            st.session_state.last_result = f"<div class='big-win-anim'>💥 JACKPOT! 7️⃣7️⃣7️⃣ - Thắng {win} 💰</div>"
            st.session_state.big_win = True
        else:
            win = bet * 10
            st.session_state.balance += win
            st.session_state.last_result = f"<div class='big-win-anim'>🎉 Nổ hũ! {slots[0]*3} - Thắng {win} 💰</div>"
            st.session_state.big_win = True
    elif slots[0] == slots[1] or slots[1] == slots[2] or slots[0] == slots[2]:
        win = bet * 2
        st.session_state.balance += win
        st.session_state.last_result = f"<div style='color:#ffe600;text-align:center;font-weight:bold;'>✨ Trúng nhỏ! Thắng {win} 💰</div>"
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
