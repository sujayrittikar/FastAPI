from fastapi import FastAPI

app = FastAPI()

# Home Page
@app.get("/")
def index():
    return {"name": "First Data"}