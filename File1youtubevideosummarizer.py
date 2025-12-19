import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import re

st.set_page_config(page_title="Vibe Summarizer", page_icon="📺")

st.title("📺 YouTube Vibe Summarizer")

video_url = st.text_input("Enter YouTube Video URL:")

def extract_video_id(url):
    # This regex is more robust for different types of YT links
        pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
            match = re.search(pattern, url)
                return match.group(1) if match else None

                if video_url:
                    video_id = extract_video_id(video_url)
                        
                            if video_id:
                                    try:
                                                with st.spinner('Grabbing the transcript vibes...'):
                                                                # Try fetching the transcript
                                                                                transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
                                                                                                full_text = " ".join([t['text'] for t in transcript_list])
                                                                                                                
                                                                                                                                # Vibe Summary Logic (Placeholder for AI)
                                                                                                                                                summary_points = [
                                                                                                                                                                    "Main topic introduced",
                                                                                                                                                                                        "Key technical details explained",
                                                                                                                                                                                                            "Practical application shown",
                                                                                                                                                                                                                                "Final summary and wrap-up"
                                                                                                                                                                                                                                                ]

                                                                                                                                                                                                                                                                st.subheader("Summary Checklist")
                                                                                                                                                                                                                                                                                for point in summary_points:
                                                                                                                                                                                                                                                                                                    st.checkbox(point)
                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                except Exception as e:
                                                                                                                                                                                                                                                                                                                                            st.error("YouTube blocked the automatic transcript grab.")
                                                                                                                                                                                                                                                                                                                                                        st.info("💡 Vibe Tip: Try a video that definitely has English CC enabled, or we can update the code to use a 'Cookie' file to bypass the block.")
                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                    st.warning("Please enter a valid YouTube URL.")
                                                                                                                                                                                                                                                                                                                                                                    