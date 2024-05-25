import streamlit as st
from pytube import YouTube
import os

st.title("--YOUTUBE VIDEO DOWNLOADER--")
link = st.text_input("Enter The Link For The Required Video")
button = st.button("Download")

if button:
    if link:
        with st.spinner("Downloading..."):
            try:
                yt = YouTube(link)
                stream = yt.streams.get_highest_resolution()
                output_path = stream.download()  # Download the video
                st.success("Download Complete!")
                
                # Provide a download button for the downloaded file
                with open(output_path, 'rb') as file:
                    st.download_button(label="Download Video", data=file, file_name=os.path.basename(output_path), mime='video/mp4')

            except Exception as e:
                st.error(f'Error: {str(e)}')
    else:
        st.error("Please Add Link.")
