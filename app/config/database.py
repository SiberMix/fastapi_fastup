from contextlib import contextmanager
from typing import Callable

from dotenv import load_dotenv
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config.settings import db_host, db_name, db_password, db_port, db_user

engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

metadata = MetaData()

Base = declarative_base(metadata=metadata, name="Base")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session():
    """Starts a database session as a context manager."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
