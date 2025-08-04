from app.chats.schemas import ChatMessage
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def read_chats():
    return {"message": "List of chats"}

@router.post('/')
async def create_chat(chat_message: ChatMessage):
    return chat_message

@router.get('/{chat_id}')
async def read_chat(chat_id: int):
    return {"message": f"Details of chats {chat_id}"}

@router.put('/{chat_id}')
async def update_chat(chat_id: int, chat_message: ChatMessage):
    return {"message": f"Chat {chat_id} updated", "chats": chat_message}

@router.delete('/{chat_id}')
async def delete_chat(chat_id: int):
    return {"message": f"Chat {chat_id} deleted"}