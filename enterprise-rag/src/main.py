cat > src/main.py <<'EOF'
from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Knowledge Intelligence Platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "Enterprise Knowledge Intelligence Platform",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.get("/api/v1/chat")
def chat(message: str):
    return {
        "question": message,
        "answer": "RAG pipeline is not connected yet.",
        "citations": [],
    }
EOF