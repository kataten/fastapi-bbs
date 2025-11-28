from fastapi import FastAPI
from app.routers import threads,posts
from app.database import engine
from app.models.thread import Base as ThreadBase
from app.models.post import Base as PostBase

app = FastAPI(title="BBS API - Step1")

app.include_router(threads.router)
app.include_router(posts.router)
app.include_router(posts.threads_router)

ThreadBase.metadata.create_all(bind=engine)
PostBase.metadata.create_all(bind=engine)