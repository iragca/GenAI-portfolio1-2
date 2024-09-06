import streamlit as st

video_file = open('/config/DS314/portfolio1/assets/video/kot.webm', 'rb')

# Read the video file
video_bytes = video_file.read()

# Display the video
st.video(video_bytes)

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

