from fastapi import FastAPI, Request
from app.webhook import handle_webhook

app = FastAPI(title="CodeGuard Platform")

@app.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()
    return handle_webhook(payload)
