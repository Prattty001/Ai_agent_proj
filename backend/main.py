from fastapi import FastAPI
from backend.routes.validate import router

app = FastAPI(
    title="AI Data Validation Agent",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "AI Data Validation Agent is running."
    }   