from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from app.models.base import Base


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
    created_at = Column(DateTime, nullable=False)  # Timestamp for when the task was created
    updated_at = Column(DateTime, nullable=True)  # Timestamp for when the task was last updated
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)

    project = relationship('Project', back_populates='tasks')
    assignee = relationship('User', back_populates='tasks')
    tags = relationship('Tag', secondary=association_table, back_populates='tasks')


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    tasks = relationship('Task', secondary=association_table, back_populates='tags')
