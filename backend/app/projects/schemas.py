from pydantic import BaseModel
from datetime import datetime
from app.tasks.schemas import TaskResponse


class ProjectRequest(BaseModel):
    name: str
    description: str
    author_id: int


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime | None
    author: str
    tasks: list[TaskResponse]

    class Config:
        orm_mode = True
        from_attributes = True