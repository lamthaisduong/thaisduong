import streamlit as st

st.set_page_config(page_title="Zing MP3 Mini", page_icon="🎶")
st.markdown("<h1 style='text-align:center; color:#8e44ad;'>🎶 Zing MP3 Mini</h1>", unsafe_allow_html=True)

# Danh sách nhạc mẫu (bạn cần có các file mp3 này trong thư mục)
songs = [
    {
        "title": "Chung Ta Cua Hien Tai",
        "artist": "Son Tung M-TP",
        "cover": "https://avatar-ex-swe.nixcdn.com/song/2021/01/02/2/8/1/2/1609570641142_500.jpg",
        "file": "chung_ta_cua_hien_tai.mp3"
    },
    {
        "title": "Co Chac Yeu La Day",
        "artist": "Son Tung M-TP",
        "cover": "https://avatar-ex-swe.nixcdn.com/song/2020/07/05/9/5/2/1/1593934983842_500.jpg",
        "file": "co_chac_yeu_la_day.mp3"
    },
    {
        "title": "Hay Trao Cho Anh",
        "artist": "Son Tung M-TP, Snoop Dogg",
        "cover": "https://avatar-ex-swe.nixcdn.com/song/2019/07/01/9/8/1/2/1561972688863_500.jpg",
        "file": "hay_trao_cho_anh.mp3"
    }
]

cols = st.columns(3)
for i, song in enumerate(songs):
    with cols[i]:
        st.image(song["cover"], use_column_width=True)
        st.markdown(f"**{song['title']}**<br><span style='color:gray'>{song['artist']}</span>", unsafe_allow_html=True)
        if st.button("Nghe ngay", key=f"play_{i}"):
            st.session_state["playing"] = i

# Hiển thị trình phát nhạc khi chọn
if "playing" in st.session_state:
    idx = st.session_state["playing"]
    st.markdown("---")
    st.markdown(f"### Đang phát: {songs[idx]['title']} - {songs[idx]['artist']}")
    try:
        audio_file = open(songs[idx]["file"], "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
    except FileNotFoundError:
        st.error("Không tìm thấy file mp3. Vui lòng thêm file mp3 vào thư mục dự án.")
