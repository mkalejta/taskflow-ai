from app.chats.schemas import ChatRequest, ChatResponse, MessageResponse, MessageRequest
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
import app.chats.services as cs

router = APIRouter()

@router.get('/{user_id}', response_model=list[ChatResponse])
async def read_chats(user_id: int, db: Session = Depends(get_db)):
    return cs.chats_by_user_id(user_id, db)

@router.get('/{chat_id}/chat', response_model=ChatResponse)
async def read_chat(chat_id: int, db: Session = Depends(get_db)):
    return cs.chat_by_id(chat_id, db)

@router.post('/', response_model=ChatResponse)
async def create_chat(chat: ChatRequest, message: MessageRequest, db: Session = Depends(get_db)):
    return cs.create_chat(chat, message, db)

@router.put('/{chat_id}', response_model=ChatResponse)
async def update_chat(chat_id: int, chat: ChatRequest, db: Session = Depends(get_db)):
    return cs.update_chat(chat_id, chat, db)

@router.put('/{chat_id}/messages', response_model=MessageResponse)
async def update_messages(chat_id: int, message: MessageRequest, db: Session = Depends(get_db)):
    return cs.update_messages(chat_id, message, db)

@router.delete('/{chat_id}', status_code=204)
async def delete_chat(chat_id: int, db: Session = Depends(get_db)):
    cs.delete_chat(chat_id, db)