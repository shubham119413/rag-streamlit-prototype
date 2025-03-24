# 🎓 AI-Powered Q&A System with FastAPI + Streamlit

This project is a Retrieval-Augmented Generation (RAG) system built using:

- ✅ **FastAPI** for backend API  
- ✅ **Streamlit** for the user interface  
- ✅ **Whisper** for audio/video transcription  
- ✅ **SentenceTransformers + FAISS** for embeddings and vector search  
- ✅ **Gemini 2.0 Flash** for AI-generated answers

---

## 📦 Features

- Upload **PDFs**, **audio**, or **video files** via the Streamlit UI  
- Transcribe audio and video using **Whisper**  
- Extract text from PDFs  
- Generate text embeddings and store using **FAISS**  
- Ask questions, get answers powered by **Gemini 2.0 Flash**

---

## 🚀 How to Use

### 1. Start the FastAPI server
    uvicorn main:app --reload

### 2. Start the Streamlit UI
    streamlit run app.py

### 3. Open the Streamlit app in your browser:
- Upload files  
- Ask questions  
- Get AI-powered answers 🚀

---

## 🧠 Requirements

Install dependencies with:
    pip install -r requirements.txt

Note: `numpy` must be <= 1.25 for compatibility with Whisper and Numba.

---

## 📁 Project Structure

    .
    ├── main.py             # FastAPI backend
    ├── app.py              # Streamlit UI
    ├── requirements.txt    # All dependencies
    ├── README.md           # You're reading it!
    ├── uploads/            # Folder for uploaded files
    ├── processed_text/     # Transcribed and extracted text

---

## ⚠️ Notes

- Make sure to set your **Gemini API key** in a `.env` file  
- Uses `moviepy` to handle video processing

---

## 🧑‍💻 Author

**Shubham Agarwal**  
🔗 [GitHub Profile](https://github.com/shubham119413)

---

## 📄 License

MIT License
