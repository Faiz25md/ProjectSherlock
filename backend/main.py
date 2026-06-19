from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to Project Sherlock"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }