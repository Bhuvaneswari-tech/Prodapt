from fastapi import FastAPI
from app.middleware.cors import add_cors_middleware
from app.middleware.exception import exception_handler
from app.controllers import category_controller, customer_controller, order_controller, product_controller

app = FastAPI()

add_cors_middleware(app)
app.add_exception_handler(Exception, exception_handler)

app.include_router(category_controller.router, prefix="/categories", tags=["Categories"])
app.include_router(customer_controller.router, prefix="/customers", tags=["Customers"])
app.include_router(order_controller.router, prefix="/orders", tags=["Orders"])
app.include_router(product_controller.router, prefix="/products", tags=["Products"])

@app.get("/")
def root():
    return {"message": "Ecommerce FastAPI is running"}
