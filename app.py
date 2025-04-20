import streamlit as st
from utils import generate_video_from_script

st.set_page_config(page_title="AI Video Generator", layout="centered")

st.title("🧠📹 AI Video Generator")
st.write("Tạo video từ văn bản với AI")

script = st.text_area("✏️ Nhập nội dung văn bản:")

if st.button("🎬 Tạo video"):
    if script.strip() == "":
        st.warning("Vui lòng nhập nội dung trước khi tạo video.")
    else:
        with st.spinner("Đang tạo video, vui lòng chờ..."):
            video_path = generate_video_from_script(script)
            st.success("✅ Video đã được tạo!")
            st.video(video_path)
