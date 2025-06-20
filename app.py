import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="We and AI", layout="centered")

# --- Title ---
st.markdown("<h1 style='text-align:center; color:#4A90E2;'>🌍 We and AI Around Us 🌍</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px; color: #FF69B4;'>🔍 Explore the impact of AI through visuals</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Image Display Area ---
image_folder = "images"
video_folder = "videos"

# Dictionary for image selections
image_files = {
    "📸 Shop & AI": "ai_makeup.jpg",
    "🌆 Health & AI": "ai_health.jpg",
    "🤖 Child & AI": "ai_children.jpg",
    "👨‍👩‍👧‍👦 Uni & AI": "ai_study.jpg",
    "📱 Lab & AI": "ai_lab.jpg"
}

st.markdown("<h3 style='color:#FF0000;'>🖼️ Select an image to display</h3>", unsafe_allow_html=True)


# Create columns for image buttons
cols = st.columns(len(image_files))
for idx, (label, filename) in enumerate(image_files.items()):
    with cols[idx]:
        if st.button(label):
            img_path = os.path.join(image_folder, filename)
            img = Image.open(img_path)
            st.image(img, caption=f"Showing: {label}", width=500)

st.markdown("---")
st.markdown("<h3 style='color:#007BFF;'>🎬 Watch the video on AI & Technology</h3>", unsafe_allow_html=True)


if st.button("▶️ Click to Play Video"):
    video_path = os.path.join(video_folder, "ai_clip.mp4")
    with open(video_path, 'rb') as f:
        video_bytes = f.read()
        st.video(video_bytes)

st.markdown("---")
st.markdown("<p style='text-align:center; color: #32CD32; font-size:25px; font-weight:bold;'>✍️ Author: Azmat Ali Akbar</p>", unsafe_allow_html=True)
