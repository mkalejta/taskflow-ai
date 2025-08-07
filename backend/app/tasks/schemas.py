from pydantic import BaseModel
from app.enums.Priority import Priority
from app.enums.Status import Status
from datetime import datetime
from app.tags.schemas import TagResponse, TagRequest


class TaskRequest(BaseModel):
    author_id: int
    title: str
    description: str
    priority: Priority
    status: Status
    assigned_to: int
    due_to: datetime
    project_id: int
    tags: list[TagRequest]


class TaskResponse(BaseModel):
    id: int
    author: str
    title: str
    description: str
    priority: Priority
    status: Status
    assignee: str
    due_to: datetime
    created_at: datetime
    updated_at: datetime | None
    project_id: int
    tags: list[TagResponse]

    class Config:
        orm_mode = True
        from_attributes = True