from fastapi import FastAPI,Request,Response
import json
from fastapi.middleware.cors import CORSMiddleware

from main import blog_to_ipfs

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")  #Returns the status of the server
async def root():
    return {"message": "server active"}

@app.post("/blog")
async def blog_gen1(title: Request): 
    var1 = await title.json()
    return {"value":blog_to_ipfs(var1)}
