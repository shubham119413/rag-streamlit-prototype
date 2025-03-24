
import streamlit as st
import requests

# Define FastAPI base URL (Replace with your actual URL)
API_URL = "https://78c0-108-4-243-124.ngrok-free.app"  # Change this when deploying

st.title("AI-Powered Q&A")

# --- Upload Files Section ---
st.header("Upload Files (PDF, MP3, WAV, MP4, MOV)")
uploaded_files = st.file_uploader(
    "Upload one or more files", 
    type=["pdf", "mp3", "wav", "mp4", "mov"], 
    accept_multiple_files=True
)

if st.button("Upload Files"):
    if uploaded_files:
        files = [("files", (file.name, file.getvalue())) for file in uploaded_files]
        response = requests.post(f"{API_URL}/upload/", files=files)
        if response.status_code == 200:
            st.success(response.json()["message"])
        else:
            st.error(f"Upload failed: {response.text}")
    else:
        st.error("Please upload at least one file.")

# --- Ask AI Section ---
st.header("Ask AI a Question")
question = st.text_input("Ask a question based on the uploaded documents:")

if st.button("Get Answer"):
    if question:
        response = requests.post(f"{API_URL}/ask/", json={"question": question, "top_k": 3})
        if response.status_code == 200:
            st.write("**AI Answer:**", response.json().get("answer", "No answer found."))
        else:
            st.error(f"Request failed: {response.text}")
    else:
        st.error("Please enter a question.")

st.write("---")
st.write("🚀 Built with FastAPI, Gemini AI, Whisper AI, and FAISS")
