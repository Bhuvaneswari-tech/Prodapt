from fastapi import FastAPI,Depends, Header, HTTPException, status

app = FastAPI()

def verify_token(x_api_key: str = Header()):
        if x_api_key != "secret123":
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key") 
    

@app.get("/hello")
def hello(token: str = Depends(verify_token)):
        return {"message": "Hello, you are authorized!"}

# To run the app, use the command: uvicorn Ex1:app --reload
  #Uvicorn is a lightweight ASGI server used to run Python web applications like FastAPI.
#FastApi = Brain(logic)
#uvicorn = Door(handles request)

# Uvicorn is an ASGI server
# ASGI (Asynchronous Server Gateway Interface) allows handling multiple requests asynchronously.