from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.tags.schemas import TagRequest, TagResponse
import app.tags.services as ts

router = APIRouter()

@router.get("/", response_model=list[TagResponse])
async def get_tags(db: Session = Depends(get_db)):
    return ts.get_all_tags(db)

@router.get("/{tag_id}", response_model=TagResponse)
async def get_tag(tag_id: int, db: Session = Depends(get_db)):
    return ts.get_tag_by_id(tag_id, db)

@router.post("/", response_model=TagResponse)
async def add_tag(tag: TagRequest, db: Session = Depends(get_db)):
    return ts.add_tag(tag, db)

@router.put("/{tag_id}", response_model=TagResponse)
async def update_tag(tag_id: int, tag: TagRequest, db: Session = Depends(get_db)):
    return ts.update_tag(tag_id, tag, db)

@router.delete("/{tag_id}", status_code=204)
async def delete_tag(tag_id: int, db: Session = Depends(get_db)) -> None:
    ts.delete_tag(tag_id, db)