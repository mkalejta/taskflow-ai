from app.db.models import Tag
from app.tags.schemas import TagRequest, TagResponse
from sqlalchemy.orm import Session
from fastapi import HTTPException


def convert_tag_to_response(tag: Tag) -> TagResponse:
    """Converts Tag ORM object to TagResponse object"""
    tag_dict = {
        "id": tag.id,
        "name": tag.name
    }
    return TagResponse(**tag_dict)

def get_all_tags(db: Session) -> list[TagResponse]:
    tags = db.query(Tag).all()
    return [convert_tag_to_response(tag) for tag in tags]


def get_tag_by_id(tag_id: int, db: Session) -> TagResponse:
    tag = db.get(Tag, tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found!")
    return convert_tag_to_response(tag)

def add_tag(tag: TagRequest, db: Session) -> TagResponse:
    new_tag = Tag(**tag.dict())
    if_exists = db.query(Tag).filter(Tag.name == tag.name).first()
    if if_exists is not None:
        raise HTTPException(status_code=409, detail="Tag with this name already exists!")
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return convert_tag_to_response(new_tag)

def update_tag(tag_id: int, tag: TagRequest, db: Session) -> TagResponse:
    old_tag = db.get(Tag, tag_id)
    if old_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found!")
    if_exists = db.query(Tag).filter(Tag.name == tag.name).first()
    if if_exists is not None:
        raise HTTPException(status_code=409, detail="Tag with new name already exists!")
    setattr(old_tag, 'name', tag.name)
    db.commit()
    db.refresh(old_tag)
    return convert_tag_to_response(old_tag)

def delete_tag(tag_id: int, db: Session) -> None:
    tag = db.get(Tag, tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found!")
    db.delete(tag)
    db.commit()