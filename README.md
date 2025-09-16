# 🤖 HR Policy RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with **LangChain, FAISS, Groq LLM, FastAPI, and Streamlit**.  
This bot allows employees to ask questions about HR policies, and it retrieves answers directly from the company’s HR Policy PDF.

---

## 🚀 Features
- 📑 Ingests HR Policy PDF and creates a searchable FAISS index
- 🔎 Retrieves the most relevant policy chunks for each query
- 🧠 Uses Groq LLM (`mixtral-8x7b-instruct`) for natural language answers
- ⚡ FastAPI backend serving retrieval + LLM responses
- 🎨 Streamlit frontend for a simple, interactive chat UI
- 🖥️ One-click launcher (`run_all.bat`) for Windows

---

## 📂 Project Structure
hr-rag/
├─ .env # API key (not shared in repo)
├─ requirements-all.txt # Install backend + frontend deps
├─ run_all.bat # One-click start script (Windows)
├─ backend/
│ ├─ requirements.txt # Backend-only deps
│ ├─ app/
│ │ ├─ main.py # FastAPI backend
│ │ ├─ llm_client.py # Groq API call
│ │ ├─ prompt_template.txt # Prompt template
├─ frontend/
│ ├─ app.py # Streamlit frontend
├─ chunks.pkl # Saved chunks (generated in Jupyter)
├─ faiss_index/ # Saved FAISS index (generated in Jupyter)
