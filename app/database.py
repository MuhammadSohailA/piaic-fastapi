# from sqlalchemy.orm import session
import os

from sqlmodel import Session, SQLModel, create_engine

engine = create_engine("postgresql://postgres:aa123@localhost:5432/learn_fastapi")


def get_db():
    with Session(engine) as session:
        yield session


async def init_db():
    SQLModel.metadata.create_all(engine)
