from fastapi import FastAPI
from app.agent import run_agent

app = FastAPI()

@app.post("/alert")
async def receive_alert(alert: dict):
    decision = run_agent(alert)
    return decision