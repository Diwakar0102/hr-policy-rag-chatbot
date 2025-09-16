from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from llm_client import call_llm

# Load FAISS index + embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# FastAPI app
app = FastAPI(title="HR RAG Chatbot")

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query_endpoint(req: QueryRequest):
    try:
        # 1. Retrieve context
        docs = retriever.invoke(req.query)
        context = "\n\n".join([f"[Page {d.metadata.get('page')}] {d.page_content}" for d in docs])

        # 2. Load prompt template
        with open("prompt_template.txt") as f:
            template = f.read()
        prompt = template.format(context=context, query=req.query)

        # 3. Call LLM
        answer = call_llm(prompt)

        return {
            "query": req.query,
            "answer": answer,
            "sources": [d.metadata for d in docs]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}
