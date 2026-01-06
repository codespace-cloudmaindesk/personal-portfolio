from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager
from app.core import database


@contextmanager
def override_database_url(url: str):
    """
    Temporarily override the database engine and session factory for testing.
    """
    # Save original engine and session factory
    original_engine = database.engine
    original_session_factory = database.SessionLocal

    # Create new engine and session factory
    database.engine = create_engine(
        url,
        connect_args={"check_same_thread": False} if "sqlite" in url else {},
        pool_pre_ping=True,
    )
    database.SessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=database.engine
    )

    try:
        yield
    finally:
        # Restore original engine and session factory
        database.engine = original_engine
        database.SessionLocal = original_session_factory


def test_get_db_session():
    """
    Test that get_db() yields a SQLAlchemy session and closes it properly.
    Uses in-memory SQLite database for isolation.
    """
    test_url = "sqlite:///:memory:"
    with override_database_url(test_url):
        db_gen = database.get_db()
        db: Session = next(db_gen)
        assert isinstance(db, Session)
        result = db.execute(text("SELECT 1")).scalar()
        assert result == 1

        # Close generator properly
        try:
            next(db_gen)
        except StopIteration:
            pass


def test_get_db_rollback_on_error(mocker):
    """
    Test that get_db() rolls back the session if commit fails.
    """
    test_url = "sqlite:///:memory:"
    with override_database_url(test_url):
        db_gen = database.get_db()
        db: Session = next(db_gen)

        # Mock commit to raise an exception
        mocker.patch.object(db, "commit", side_effect=SQLAlchemyError("Commit failed"))
        rollback_spy = mocker.spy(db, "rollback")

        try:
            next(db_gen)  # triggers commit inside get_db()
        except Exception:
            pass

        rollback_spy.assert_called_once()


def test_use_local_db_flag(monkeypatch):
    """
    Test that get_use_local_db() and get_database_url() reflect correct behavior.
    """
    # Test SQLite detection
    monkeypatch.setattr(database.settings, "DATABASE_URL_LOCAL", "sqlite:///./test.db")
    monkeypatch.setattr(
        database.settings,
        "DATABASE_URL",
        "postgresql+psycopg2://user:pass@localhost/db",
    )

    assert database.get_use_local_db() is True
    assert "sqlite" in database.get_database_url()

    # Now simulate production fallback
    monkeypatch.setattr(
        database.settings,
        "DATABASE_URL_LOCAL",
        "postgresql+psycopg2://user:pass@localhost/db",
    )
    monkeypatch.setattr(
        database.settings,
        "DATABASE_URL",
        "postgresql+psycopg2://user:pass@localhost/db",
    )

    assert database.get_use_local_db() is False
    assert "postgresql" in database.get_database_url()


def test_session_local_creates_session():
    """
    Test that SessionLocal creates a working session bound to an in-memory SQLite engine.
    """
    test_url = "sqlite:///:memory:"
    with override_database_url(test_url):
        session_factory = database.SessionLocal
        db = session_factory()
        assert isinstance(db, Session)
        result = db.execute(text("SELECT 1")).scalar()
        assert result == 1
        db.close()
