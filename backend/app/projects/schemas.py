from pydantic import BaseModel
from datetime import datetime


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

    class Config:
        orm_mode = True