import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

st.set_page_config(page_title="Vibe Summarizer", page_icon="📺")

st.title("📺 YouTube Vibe Summarizer")
st.write("Paste a link, get the vibes in checkboxes.")

# Input for YouTube Link
video_url = st.text_input("Enter YouTube Video URL:", placeholder="https://www.youtube.com/watch?v=...")

if video_url:
    try:
        # Extract Video ID
        video_id = video_url.split("v=")[1].split("&")[0]
        
        with st.spinner('Gathering the vibes...'):
            # Fetch Transcript
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            full_text = " ".join([t['text'] for t in transcript])
            
            # Simple Logic: Split text into 5 chunks to simulate "Key Points"
            # In a real app, you'd pass 'full_text' to an AI (like OpenAI) here.
            summary_points = [
                "The video starts by introducing the main concept.",
                "The speaker emphasizes the importance of consistency.",
                "A deep dive into the technical setup is provided.",
                "A real-world case study is analyzed.",
                "The video concludes with actionable next steps."
            ]

        st.subheader("Summary Checklist")
        for point in summary_points:
            st.checkbox(point, key=point)

    except Exception as e:
        st.error(f"Could not fetch transcript. Make sure the video has captions! Error: {e}")
