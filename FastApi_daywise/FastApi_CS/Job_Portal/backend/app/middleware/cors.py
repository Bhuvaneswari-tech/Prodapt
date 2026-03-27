from fastapi.middleware.cors import CORSMiddleware

def add_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Or specify your frontend URL: ["http://localhost:5174"]
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)