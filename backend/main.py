from fastapi import FastAPI
from shared.tools import system_health

app = FastAPI()

@app.get("/health")
def health():
    return system_health()
