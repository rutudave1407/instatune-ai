import streamlit as st
import requests

st.title("🎬 Bollywood AI - Social Media Suggester")

# Inputs
uploaded_files = st.file_uploader("Upload Images (Max 5)", accept_multiple_files=True, type=['jpg', 'png'])
if len(uploaded_files) > 5:
    st.error(f"❌ Limit Exceeded: You uploaded {len(uploaded_files)} images. Please remove {len(uploaded_files) - 5} image(s) to proceed.")
    st.stop()  # This kills the app execution here so no API call is made

keywords = st.multiselect("Vibe", ["Love", "Birthday", "Party", "Friendship", "Travel","wedding", "sad"])
context = st.text_input("Additional Prompt Detail (e.g. 'Slow and romantic')")

# Duration Feature added
duration = st.radio("Target Video Duration", ["5 sec", "15 sec", "30 sec", "60 sec"], horizontal=True)

if st.button("Get Song"):
    if not uploaded_files:
        st.warning("Please upload at least one image.")
    else:
        # Prepare multipart/form-data
        files = [("files", (f.name, f.getvalue(), f.type)) for f in uploaded_files]
        data = {"keywords": ",".join(keywords), "user_context": context, "duration": duration}
        
        with st.spinner("Analyzing your images and song timing..."):
            res = requests.post("http://localhost:8000/suggest-song", data=data, files=files)
            if res.status_code == 200:
                song = res.json()
                st.subheader(f"🎵 {song['song_name']}")
                st.json(song) # Valid JSON output as requested
            else:
                st.error(f"API Error: {res.text}")