from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Agentic HoneyPot AI")

app.include_router(router)

@app.get("/")
def home():
    return {"status": "running"}
