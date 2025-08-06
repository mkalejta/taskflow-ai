from pydantic import BaseModel, EmailStr
from app.projects.schemas import ProjectResponse
from app.tasks.schemas import TaskResponse
from app.chats.schemas import ChatResponse

class UserRequest(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str
    is_active: bool
    assigned_tasks: list[TaskResponse]
    authored_tasks: list[TaskResponse]
    projects: list[ProjectResponse]
    chats: list[ChatResponse]

    class Config:
        orm_mode = True
        from_attributes = True