import logging
from fastapi import Request

async def exception_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as exc:
        logging.exception(f"Unhandled error: {exc}")
        raise
