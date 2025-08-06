from app.db.models import User
from app.users.schemas import UserResponse, UserRequest
from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from app.users.hasher import Hasher
from app.chats.schemas import ChatMessage
from app.projects.services import convert_to_project_response
from app.tasks.services import convert_task_to_response


def convert_to_user_response(user: User) -> UserResponse:
    """Converts User ORM object to UserResponse object"""
    user_dict = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "is_active": user.is_active,
        "assigned_tasks": [convert_task_to_response(t) for t in user.assigned_tasks],
        "authored_tasks": [convert_task_to_response(t) for t in user.authored_tasks],
        "projects": [convert_to_project_response(p) for p in user.projects],
        "chats": [ChatMessage.from_orm(c) for c in user.chats],
    }
    return UserResponse(**user_dict)

def get_all_users(db: Session) -> list[UserResponse]:
    users = db.query(User).options(
        joinedload(User.assigned_tasks),
        joinedload(User.authored_tasks),
        joinedload(User.projects),
        joinedload(User.chats)
    ).all()
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






