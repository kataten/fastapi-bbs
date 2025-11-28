from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from app.database import get_db
from app.models.thread import Thread
from app.schemas.thread import ThreadResponse, ThreadCreate

router = APIRouter(
    prefix="/threads",
    tags=["Threads"],
)

@router.get("/",response_model=list[ThreadResponse])
async def list_threads(db:Session = Depends(get_db)):
    threads = db.query(Thread).all()
    return threads
    
@router.get("/{thread_id}",response_model=ThreadResponse)
async def get_thread(thread_id: int, db:Session = Depends(get_db)):
    thread = db.query(Thread).filter(Thread.id == thread_id).first()
    return thread

@router.post("/",response_model=ThreadResponse)
async def create_thread(thread:ThreadCreate, db:Session = Depends(get_db)):
    new_thread = Thread(title=thread.title)
    db.add(new_thread)
    db.commit()
    db.refresh(new_thread)
    return new_thread