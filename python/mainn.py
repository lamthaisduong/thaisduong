import streamlit as st

st.title("🎵 Trình phát nhạc đơn giản với Streamlit")

st.write("Chọn một bài hát để nghe:")

audio_file = open("song.mp3", "rb")
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

st.write("Tải file mp3 tên là 'song.mp3' vào cùng thư mục với file này để nghe nhạc.")