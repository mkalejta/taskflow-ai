from sqlalchemy import Table, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.db import Base

association_table = Table('task_tags', Base.metadata,
    Column('task_id', ForeignKey('tasks.id')),
    Column('tag_id', ForeignKey('tags.id'))
)


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    priority = Column(String, nullable=False)
    status = Column(String, nullable=False)
    assigned_to = Column(Integer, ForeignKey('users.id'), nullable=True)
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)

    project = relationship('Project', back_populates='tasks')
    author = relationship('User', back_populates='authored_tasks', foreign_keys=[author_id])
    assignee = relationship('User', back_populates='assigned_tasks', foreign_keys=[assigned_to])
    tags = relationship('Tag', secondary=association_table, back_populates='tasks')


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Integer, default=1)  # 1 for active, 0 for inactive

    assigned_tasks = relationship('Task', back_populates='assignee', foreign_keys='Task.assigned_to')
    authored_tasks = relationship('Task', back_populates='author', foreign_keys='Task.author_id')
    projects = relationship('Project', back_populates='author')
    chats = relationship('Chat', back_populates='user')


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    author = relationship('User', back_populates='projects')
    tasks = relationship('Task', back_populates='project')


class Chat(Base):
    __tablename__ = 'chats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='chats')
    chat_messages = relationship('ChatMessages', back_populates='chat')


class ChatMessages(Base):
    __tablename__ = 'chat_messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, ForeignKey('chats.id'), nullable=False)
    role = Column(String, nullable=False)  # e.g., 'user', 'assistant'
    content = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    chat = relationship('Chat', back_populates='chat_messages')


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    tasks = relationship('Task', secondary=association_table, back_populates='tags')
