from importlib import reload
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from app.core import database
from contextlib import contextmanager


@contextmanager
def override_database_url(url: str):
    """
    Temporarily override the database URL for testing.

    Args:
        url (str): The database URL to use during the test.
    """
    original_url = database.DATABASE_URL
    database.DATABASE_URL = url
    # Recreate engine and session factory for the override
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
        database.DATABASE_URL = original_url
        database.engine = create_engine(
            original_url,
            connect_args=(
                {"check_same_thread": False} if "sqlite" in original_url else {}
            ),
            pool_pre_ping=True,
        )
        database.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=database.engine
        )


def test_get_db_session():
    """
    Test that get_db() yields a SQLAlchemy session and closes it properly.
    Uses in-memory SQLite database for isolation.
    """
    test_url = "sqlite:///:memory:"
    with override_database_url(test_url):
        db_gen = database.get_db()
        db: Session = next(db_gen)  # Get the session
        assert isinstance(db, Session)
        # Test that session works
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
            next(db_gen)  # this triggers commit inside get_db()
        except Exception:
            pass
        rollback_spy.assert_called_once()


def test_use_local_db_flag(monkeypatch):
    """
    Test that USE_LOCAL_DB correctly detects SQLite URLs.
    """
    monkeypatch.setattr(database.settings, "DATABASE_URL_LOCAL", "sqlite:///./test.db")
    reload(database)
    assert "sqlite" in database.settings.DATABASE_URL_LOCAL
    assert database.USE_LOCAL_DB is True

    monkeypatch.setattr(
        database.settings,
        "DATABASE_URL_LOCAL",
        "postgresql+psycopg2://user:pass@localhost/db",
    )
    reload(database)
    use_local = "sqlite" in database.settings.DATABASE_URL_LOCAL
    assert use_local is False


def test_session_local_creates_session():
    """
    Test that SessionLocal creates a working session bound to an in-memory SQLite engine.
    """
    test_url = "sqlite:///:memory:"
    with override_database_url(test_url):
        session_factory = database.SessionLocal
        db = session_factory()
        assert isinstance(db, Session)
        # Run a simple raw query
        result = db.execute(text("SELECT 1")).scalar()
        assert result == 1
        db.close()
