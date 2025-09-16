import streamlit as st
import requests

st.set_page_config(page_title="HR Policy Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 HR Policy Chatbot")
st.write("Ask me about company HR policies!")

query = st.text_input("Enter your question:")

if st.button("Ask"):
    if query.strip() == "":
        st.warning("Please enter a question.")
    else:
        try:
            # Call FastAPI backend
            response = requests.post(
                "http://127.0.0.1:8000/query",
                json={"query": query},
                timeout=30
            )
            if response.status_code == 200:
                data = response.json()
                st.success(data["answer"])
                with st.expander("📚 Sources"):
                    for src in data["sources"]:
                        st.write(src)
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"⚠️ Failed to connect to backend: {e}")
