from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.tasks.schemas import TaskRequest, TaskResponse
from app.tags.schemas import TagRequest
import app.tasks.services as ts

router = APIRouter()

@router.get('/', response_model=list[TaskResponse])
async def read_tasks(db: Session = Depends(get_db)):
    return ts.get_all_tasks(db)

@router.post('/', response_model=TaskResponse)
async def create_task(task: TaskRequest, tags: list[TagRequest], db: Session = Depends(get_db)):
    return ts.add_task(task, tags, db)

@router.get('/{task_id}', response_model=TaskResponse)
async def read_task(task_id: int, db: Session = Depends(get_db)):
    return ts.get_task_by_id(task_id, db)

@router.put('/{task_id}', response_model=TaskResponse)
async def update_task(task_id: int, task: TaskRequest, db: Session = Depends(get_db)):
    return ts.update_task_details(task_id, task, db)

@router.put('/{task_id}/tags', response_model=TaskResponse)
async def update_task(task_id: int, tags: list[TagRequest], db: Session = Depends(get_db)):
    return ts.update_task_tags(task_id, tags, db)

@router.delete('/{task_id}', status_code=204)
async def delete_task(task_id: int, db: Session = Depends(get_db)) -> None:
    ts.delete_task(task_id, db)