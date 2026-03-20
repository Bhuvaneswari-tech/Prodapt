from fastapi import FastAPI
from app.middleware.cors import add_cors
#from app.middleware.logging import LoggingMiddleware
#from app.middleware.exception import ExceptionMiddleware
from app.core.database import Database
#from app.core.logging import setup_logging
from app.controllers.user_controller import router as user_router
from app.controllers.product_controller import router as product_router
from app.controllers.order_controller import router as order_router
from app.controllers.auth_controller import router as auth_router

#setup_logging()
app = FastAPI()

add_cors(app)
#app.add_middleware(LoggingMiddleware)
#app.add_middleware(ExceptionMiddleware)

@app.on_event("startup")
def startup():
    Database.connect()

app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(auth_router)
