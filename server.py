from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from handler import user, uploadfile, home
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(uploadfile.router)
app.include_router(user.router)
app.include_router(home.router)



