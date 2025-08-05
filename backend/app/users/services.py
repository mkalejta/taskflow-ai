from app.db.models import User
from app.users.schemas import UserResponse, UserRequest
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.users.hasher import Hasher


def convert_to_user_response(user: User) -> UserResponse:
    """Converts User ORM object to UserResponse object"""
    return UserResponse.from_orm(user)


def get_all_users(db: Session) -> list[UserResponse]:
    users = db.query(User).all()
    return [convert_to_user_response(user) for user in users]


def get_user_by_id(id: int, db: Session) -> UserResponse:
    user = db.query(User).get(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found!")
    return convert_to_user_response(user)


def add_user(user: UserRequest, db: Session) -> UserResponse:
    user_data = user.dict()
    user_data.pop("password")
    new_user = User(**user_data)
    new_user.hashed_password = Hasher.get_password_hash(user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return convert_to_user_response(new_user)


def update_user(id: int, user: UserRequest, db: Session) -> UserResponse:
    old_user = db.query(User).get(id)
    if old_user is None:
        raise HTTPException(status_code=404, detail="User not found!")
    for k, v in user.dict().items():
        setattr(old_user, k, v)
    db.commit()
    db.refresh(old_user)
    return convert_to_user_response(old_user)


def delete_user(id: int, db: Session) -> None:
    user = db.query(User).get(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found!")
    db.delete(user)
    db.commit()
    return None






