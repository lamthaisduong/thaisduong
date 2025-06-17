import streamlit as st
import datetime
import random

st.set_page_config(page_title="Love Day", page_icon="❤️")

# Hiệu ứng trái tim rơi bằng HTML + CSS
st.markdown("""
<style>
.heart-fall-container {
    position: relative;
    width: 100%;
    height: 320px;
    overflow: hidden;
    background: linear-gradient(180deg, #fffbe6 0%, #ffe6f7 100%);
    border-radius: 18px;
    margin-bottom: 1.5rem;
}
.heart-fall {
    position: absolute;
    animation: fall linear infinite;
    font-size: 2.2rem;
    user-select: none;
    pointer-events: none;
}
@keyframes fall {
    0% {
        top: -40px;
        opacity: 0.7;
        transform: translateY(0) scale(1) rotate(0deg);
    }
    70% {
        opacity: 1;
    }
    100% {
        top: 320px;
        opacity: 0.2;
        transform: translateY(40px) scale(1.2) rotate(30deg);
    }
}
.love-names {
    text-align: center;
    font-size: 1.4rem;
    color: #e74c3c;
    font-weight: bold;
    margin-bottom: 0.7rem;
    letter-spacing: 1px;
}
.love-days {
    text-align: center;
    color: #e74c3c;
    font-size: 1.2rem;
    margin-bottom: 1.2rem;
}
</style>
""", unsafe_allow_html=True)

# Tạo HTML cho nhiều trái tim rơi ngẫu nhiên
def gen_hearts_html(n=18):
    html = '<div class="heart-fall-container">'
    for i in range(n):
        left = random.randint(2, 95)
        duration = random.uniform(2.5, 4.5)
        delay = random.uniform(0, 2.5)
        size = random.uniform(1.3, 2.2)
        heart = random.choice(['❤️','💖','💕','💗','💓','💞'])
        html += f'<div class="heart-fall" style="left:{left}%; animation-duration:{duration}s; animation-delay:{delay}s; font-size:{size}rem;">{heart}</div>'
    html += '</div>'
    return html

st.markdown(gen_hearts_html(22), unsafe_allow_html=True)

# Tên hai bạn
st.markdown("""
<div class="love-names">
    Lâm Thái Dương <span style="color:#ff69b4;">&nbsp;💖&nbsp;</span> Nguyễn Trần Như Ý
</div>
""", unsafe_allow_html=True)

# Đếm số ngày
start_date = datetime.date(2023, 7, 26)  # Ngày bắt đầu (bạn có thể đổi)
today = datetime.date.today()
days = (today - start_date).days
if days > 357:
    days = 357

st.markdown(
    f"<div class='love-days'>Ngày bên nhau: <b>{days}</b> / 357 ngày</div>",
    unsafe_allow_html=True
)

st.success("Chúc hai bạn luôn hạnh phúc! ❤️")

# Nhạc nền (nếu muốn, chỉ phát khi click play)
st.audio("https://cdn.pixabay.com/audio/2023/03/13/audio_128bfa6b5b.mp3")
