from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.settings import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
session_generator = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db_session():
    db = session_generator()
    try:
        yield db
    finally:
        db.close()
