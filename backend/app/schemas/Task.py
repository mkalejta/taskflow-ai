from pydantic import BaseModel
from app.enums.Priority import Priority
from app.enums.Status import Status
from datetime import datetime


class TaskRequest(BaseModel):
    id: int
    author: int
    title: str
    description: str
    priority: Priority
    status: Status
    assigned_to: int
    due_to: datetime
    created_at: datetime
    updated_at: datetime


class TaskResponse(BaseModel):
    id: int
    author: str
    title: str
    description: str
    priority: Priority
    status: Status
    assigned_to: str
    tags: list[str]
    due_to: datetime
    created_at: datetime
    updated_at: datetime