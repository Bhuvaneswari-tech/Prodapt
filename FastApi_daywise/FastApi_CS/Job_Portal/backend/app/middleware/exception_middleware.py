from fastapi.responses import JSONResponse

def custom_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"}
    )