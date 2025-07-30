from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Integer, default=1)  # 1 for active, 0 for inactive

    tasks = relationship('Task', back_populates='users')
    projects = relationship('Project', back_populates='users')
    chats = relationship('Chat', back_populates='chats')
