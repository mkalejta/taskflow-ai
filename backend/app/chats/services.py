from app.db.models import Chat, ChatMessage
from app.chats.schemas import ChatRequest, ChatResponse, MessageRequest, MessageResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

def convert_chat_to_response(chat: Chat) -> ChatResponse:
    """Converts Chat ORM object to ChatResponse object"""
    chat_dict = {
        "id": chat.id,
        "user": chat.user.full_name,
        "title": chat.title,
        "description": chat.description,
        "chat_messages": [MessageResponse.from_orm(m) for m in chat.chat_messages]
    }
    return ChatResponse(**chat_dict)

def chats_by_user_id(user_id: int, db: Session) -> list[ChatResponse]:
    chats = db.query(Chat).options(
        joinedload(Chat.user),
        joinedload(Chat.chat_messages)
    ).filter(Chat.user_id == user_id).all()
    return [convert_chat_to_response(chat) for chat in chats]

def chat_by_id(chat_id: int, db: Session) -> ChatResponse:
    chat = db.get(Chat, chat_id)
    if chat is None:
        raise HTTPException(status_code=404, detail="Chat not found!")
    return convert_chat_to_response(chat)

def create_chat(chat: ChatRequest, message: MessageRequest, db: Session) -> ChatResponse:
    chat_dict = chat.dict()
    if chat.title is None:
        chat_dict["title"] = message.content[:20] + ('...' if len(message.content) > 20 else '')   # Default title is first 20 characters of entry message + '...' if truncated
    new_chat = Chat(**chat_dict)
    db.add(new_chat)
    db.commit()
    first_message = ChatMessage(**{
        "chat_id": new_chat.id,
        "role": message.role.value,
        "content": message.content
    })
    db.add(first_message)
    db.commit()
    db.refresh(new_chat)
    db.refresh(first_message)
    return convert_chat_to_response(new_chat)

def update_chat(chat_id: int, chat: ChatRequest, db: Session) -> ChatResponse:
    old_chat = db.get(Chat, chat_id)
    if old_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found!")
    for k, v in chat.dict(exclude={'id', 'user_id'}).items():
        setattr(old_chat, k, v)
    db.commit()
    db.refresh(old_chat)
    return convert_chat_to_response(old_chat)

def update_messages(chat_id: int, message: MessageRequest, db: Session) -> MessageResponse:
    chat = db.get(Chat, chat_id)
    if chat is None:
        raise HTTPException(status_code=404, detail="Chat not found!")
    new_message = ChatMessage(**{
        "chat_id": chat_id,
        "role": message.role.value,
        "content": message.content
    })
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    db.refresh(chat)
    return MessageResponse.from_orm(new_message)

def delete_chat(chat_id: int, db: Session) -> None:
    chat = db.get(Chat, chat_id)
    if chat is None:
        raise HTTPException(status_code=404, detail="Chat not found!")
    db.delete(chat)
    db.commit()