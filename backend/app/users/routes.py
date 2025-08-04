from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def read_users():
    return {"message": "List of users"}

@router.post('/')
async def create_user(user: dict):
    return {"message": "User created", "user": user}

@router.get('/{user_id}')
async def read_user(user_id: int):
    return {"message": f"Details of user {user_id}"}

@router.put('/{user_id}')
async def update_user(user_id: int, user: dict):
    return {"message": f"User {user_id} updated", "user": user}

@router.delete('/{user_id}')
async def delete_user(user_id: int):
    return {"message": f"User {user_id} deleted"}
