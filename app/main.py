from fastapi import FastAPI
from app.routers import threads
from app.routers import posts

app = FastAPI(title="BBS API - Step1")

app.include_router(threads.router)
app.include_router(posts.router)
app.include_router(posts.thrads_router)