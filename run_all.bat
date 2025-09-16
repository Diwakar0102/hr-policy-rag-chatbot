@echo off
echo ======================================
echo 🚀 Starting HR RAG Chatbot (Backend + Frontend)
echo ======================================

REM Activate virtual environment (if you use one)
REM call venv\Scripts\activate

REM Start FastAPI backend in new terminal
start cmd /k "cd backend\app && uvicorn main:app --reload --port 8000"

REM Small delay to let backend boot up
timeout /t 5 >nul

REM Start Streamlit frontend
cd frontend
streamlit run app.py

pause
