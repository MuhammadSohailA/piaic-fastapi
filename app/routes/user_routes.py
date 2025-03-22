from database import get_db
from models.user_model import CreateUsers, Users
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends

user_router = APIRouter(prefix="/api", tags=["users"])


@user_router.get("/users")
async def get_users(db: Session = Depends(get_db)):

    users = db.query(Users).all()
    if len(users) == 0:
        return {"message": "No users found"}
    return users


@user_router.post("/users/create")
async def create_user(user: CreateUsers, db: Session = Depends(get_db)):

    user_db = Users(**user.dict())
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db
