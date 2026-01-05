from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

USE_LOCAL_DB = "sqlite" in settings.DATABASE_URL_LOCAL

"""
Determine whether to use the local SQLite database or the production PostgreSQL database.

- True → Use SQLite (local development or testing)
- False → Use PostgreSQL (production / Docker / cloud)
"""
DATABASE_URL = settings.DATABASE_URL_LOCAL if USE_LOCAL_DB else settings.DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine        
)

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise
    finally:
        db.close()
