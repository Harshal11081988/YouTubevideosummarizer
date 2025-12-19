import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import re

# Set up the page style
st.set_page_config(page_title="Vibe Summarizer", page_icon="📺")

st.title("📺 YouTube Vibe Summarizer")
st.write("Paste a link below to get a checklist of the key vibes.")

def extract_video_id(url):
    """
    Extracts the video ID from various YouTube URL formats.
    """
    pattern = r'(?:v=|\/|be\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

# User Input
video_url = st.text_input("Enter YouTube Video URL:", placeholder="https://www.youtube.com/watch?v=...")

if video_url:
    video_id = extract_video_id(video_url)
    
    if video_id:
        try:
            with st.spinner('Reading the transcript...'):
                # Fetch the transcript text
                transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
                
                # In 'Vibe Coding', we can eventually send this text to Gemini or OpenAI
                # For now, we simulate the summary points based on the transcript success
                summary_points = [
                    "Introduction to the core topic.",
                    "Detailed breakdown of the first major point.",
                    "Secondary insights and supporting evidence.",
                    "Common pitfalls or mistakes to avoid.",
                    "Conclusion and final takeaways."
                ]

                st.subheader("✅ Summary Checklist")
                st.info("Check off these points as you review them:")
                
                for point in summary_points:
                    st.checkbox(point)
                    
        except Exception as e:
            st.error("Error: Could not fetch transcript.")
            st.warning("Note: This often happens if the video has 'Auto-generated' captions only or if YouTube is blocking the request. Try a video with manual English captions!")
            st.write(f"Technical details: {e}")
    else:
        st.warning("That doesn't look like a valid YouTube link. Please check the URL.")

# Footer Vibe
st.divider()
st.caption("Built with Vibe Coding ☮️ - Store this on GitHub to deploy!")
 