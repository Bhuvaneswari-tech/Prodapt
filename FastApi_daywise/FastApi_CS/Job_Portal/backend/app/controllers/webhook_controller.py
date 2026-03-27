from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/webhook")
async def webhook_listener(request: Request):
    payload = await request.json()
    print("Webhook received:", payload)
    return {"status": "received", "payload": payload}
