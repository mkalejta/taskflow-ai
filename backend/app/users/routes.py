from fastapi import APIRouter, Depends
from app.db.deps import get_db
from sqlalchemy.orm import Session
import app.users.services as us
from app.users.schemas import UserResponse, UserRequest
from app.db.models import User
from app.auth.dependencies import get_current_user


router = APIRouter()

@router.get('/', response_model=list[UserResponse])
async def read_users(db: Session = Depends(get_db)):
    return us.get_all_users(db)

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return us.convert_to_user_response(current_user)

@router.get('/{user_id}', response_model=UserResponse)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    return us.get_user_by_id(user_id, db)

@router.put('/{user_id}', response_model=UserResponse)
async def update_user(user_id: int, user: UserRequest, db: Session = Depends(get_db)):
    return us.update_user(user_id, user, db)

@router.delete('/{user_id}', status_code=204)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    us.delete_user(user_id, db)
