import streamlit as st
import datetime

st.set_page_config(page_title="Love Days", page_icon="❤️")

# Hiệu ứng trái tim động và tên hai bạn
st.markdown("""
<style>
.heart {
    font-size: 3rem;
    animation: beat 0.7s infinite alternate;
    display: flex;
    justify-content: center;
    margin-bottom: 0.5rem;
}
@keyframes beat {
    0% { transform: scale(1);}
    100% { transform: scale(1.25);}
}
.love-names {
    text-align: center;
    font-size: 1.3rem;
    color: #e74c3c;
    font-weight: bold;
    margin-bottom: 1.2rem;
    letter-spacing: 1px;
}
</style>
<div class="heart">❤️</div>
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
st.markdown(f"<h2 style='text-align:center;color:#e74c3c;'>Ngày bên nhau: <b>{days}</b> / 357 ngày</h2>", unsafe_allow_html=True)
