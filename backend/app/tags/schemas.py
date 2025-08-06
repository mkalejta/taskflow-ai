from pydantic import BaseModel


class TagRequest(BaseModel):
    name: str


class TagResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        from_attributes = True