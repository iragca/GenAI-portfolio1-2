import streamlit as st

kot_vid_url  = 'https://git.gari-homelab.party/CA_Irag/asset-dump/raw/branch/main/portfolio1/assets/video/kot.webm'
# Read the video file
video_bytes = video_file.read()

# Display the video
st.video(kot_vid_url)

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

