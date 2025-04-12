from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

from config import settings

engine = create_engine(settings.database_url)
session_creater = sessionmaker(engine, class_=Session, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = session_creater()
    try:
        yield db

    finally:
        db.close()


def create_db():
    Base.metadata.create_all(engine)
    

def drop_db():
    Base.metadata.drop_all(engine)


# Async

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession

async_engine = create_async_engine(settings.async_database_url)
async_session_creater = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)
