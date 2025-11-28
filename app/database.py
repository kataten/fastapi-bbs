from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///./bbs.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}#SQLiteの場合だけ必要
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#===========================
#DBセッション(依存性注入用)
#===========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()