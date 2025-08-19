from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.dependencies import authenticate_user, get_user_with_username, get_user_with_email
from app.auth.schemas import Token, UserCreate, UserResponse
from app.auth.utils import get_password_hash, create_access_token
from app.db.models import User
from app.db.deps import get_db

router = APIRouter()

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    user_with_same_username = get_user_with_username(db, username=user.username)
    if user_with_same_username is not None:
        raise HTTPException(status_code=400, detail="User with this username already exists!")
    user_with_same_email = get_user_with_email(db, email=user.email)
    if user_with_same_email is not None:
        raise HTTPException(status_code=400, detail="User with this email already exists!")
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password, email=user.email, full_name=user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user