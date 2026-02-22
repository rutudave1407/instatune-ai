import streamlit as st
import requests
from PIL import Image

st.title("🎵 Bollywood AI Song Recommender")

MAX_FILES = 5
uploaded_files = st.file_uploader(
    "Upload up to 5 images",
    accept_multiple_files=True,
    type=["jpg", "png", "jpeg"]
)

if uploaded_files and len(uploaded_files) <= 5:
    st.subheader("📷 Selected Images")

    cols = st.columns(min(5, len(uploaded_files)))

    for idx, file in enumerate(uploaded_files):
        img = Image.open(file)
        cols[idx].image(img, use_container_width=True)

if uploaded_files and len(uploaded_files) > MAX_FILES:
    st.error("❌ Maximum 5 images allowed. Please remove extra files.")
    st.caption(f"📸 {len(uploaded_files)} / 5 images uploaded")
    st.stop() 
    
if uploaded_files:
    st.caption(f"📸 {len(uploaded_files)} / 5 images uploaded")
    

keywords = st.text_input("Keywords (optional)")
prompt = st.text_input("One-line prompt")
duration = st.selectbox("Duration", [5, 10, 15, 30])

if st.button("Get Song Recommendation"):

    # ✅ Validation: at least 1 image
    if not uploaded_files:
        st.error("❌ Please upload at least one image.")
        st.stop()

    # ✅ Validation: max 5 images
    if len(uploaded_files) > 5:
        st.error("❌ You can upload a maximum of 5 images only.")
        st.stop()

    # Prepare files
    files = [
        ("images", (f.name, f.getvalue(), f.type))
        for f in uploaded_files
    ]

    try:
        response = requests.post(
            "http://localhost:8000/recommend",
            files=files,
            data={
                "keywords": keywords,
                "prompt": prompt,
                "duration": duration
            },
            timeout=120
        )

        st.json(response.json())

    except requests.exceptions.ConnectionError:
        st.error("⚠️ Backend server is not running. Start FastAPI first.")