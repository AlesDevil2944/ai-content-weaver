from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router as api_router

app = FastAPI(
    title="AI Content Weaver API",
    description="API for generating and optimizing content.",
    version="1.0.0"
)

# This part is the security guard, letting our website (from localhost:5173)
# talk to our server (at localhost:8000).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # The URL of our frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "AI Content Weaver API is running."}