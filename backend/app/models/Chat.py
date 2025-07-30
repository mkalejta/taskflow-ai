from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.base import Base

class Chat(Base):
    __tablename__ = 'chats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='chats')
    chat_messages = relationship('ChatMessages', back_populates='chats')


class ChatMessages(Base):
    __tablename__ = 'chat_messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, ForeignKey('chats.id'), nullable=False)
    role = Column(String, nullable=False)  # e.g., 'user', 'assistant'
    content = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)  # Timestamp for when the message was created

    chat = relationship('Chat', back_populates='chat_messages')
