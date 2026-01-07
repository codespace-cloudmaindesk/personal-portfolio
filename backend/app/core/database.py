from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from app.core.config import get_settings

settings = get_settings()


def get_use_local_db() -> bool:
    """Check if the local database (SQLite) should be used."""
    return "sqlite" in settings.DATABASE_URL_LOCAL


def get_database_url() -> str:
    """Return the active database URL depending on USE_LOCAL_DB."""
    return settings.DATABASE_URL_LOCAL if get_use_local_db() else settings.DATABASE_URL


engine = create_engine(
    get_database_url(),
    connect_args={"check_same_thread": False} if "sqlite" in get_database_url() else {},
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
