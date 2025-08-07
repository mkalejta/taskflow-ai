from app.db.models import Task, Tag
from app.tasks.schemas import TaskRequest, TaskResponse
from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from app.tags.schemas import TagResponse

def convert_task_to_response(task: Task) -> TaskResponse:
    """Converts Task ORM object to TaskResponse object"""
    task_dict = {
        "id": task.id,
        "author": task.author.full_name,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "status": task.status,
        "assignee": task.assignee.full_name,
        "due_to": task.due_to,
        "created_at": task.created_at,
        "updated_at": task.updated_at,
        "project_id": task.project_id,
        "tags": [TagResponse.from_orm(t) for t in task.tags]
    }
    return TaskResponse(**task_dict)


def get_all_tasks(db: Session) -> list[TaskResponse]:
    tasks = db.query(Task).options(
        joinedload(Task.author),
        joinedload(Task.assignee),
        joinedload(Task.tags)
    ).all()  # automatic data attachment from 'users' table to sent less request to db
    return [convert_task_to_response(t) for t in tasks]

def get_task_by_id(id: int, db: Session) -> TaskResponse:
    task = db.get(Task, id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found!")
    return convert_task_to_response(task)

def add_task(task: TaskRequest, db: Session) -> TaskResponse:
    task_data = task.dict(exclude={'tags'})
    task_data['priority'] = task_data['priority'].value
    task_data['status'] = task_data['status'].value
    new_task = Task(**task_data)
    # For each TagRequest in tags, there is check if it exists. If not first we need to add new Tag.
    tags = []
    for tag_req in task.tags:
        tag = db.query(Tag).filter_by(name=tag_req.name).first()
        if not tag:
            tag = Tag(name=tag_req.name)
            db.add(tag)
            db.flush()
        tags.append(tag)
    new_task.tags = tags
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return convert_task_to_response(new_task)

def update_task(id: int, task: TaskRequest, db: Session) -> TaskResponse:
    old_task = db.get(Task, id)
    if old_task is None:
        raise HTTPException(status_code=404, detail="Task not found!")
    task_data = task.dict(exclude={'author_id', 'project_id'})
    task_data['priority'] = task_data['priority'].value
    task_data['status'] = task_data['status'].value
    for k, v in task_data.items():
        setattr(old_task, k, v)
    db.commit()
    db.refresh(old_task)
    return convert_task_to_response(old_task)

def delete_task(id: int, db: Session) -> None:
    task = db.get(Task, id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found!")
    db.delete(task)
    db.commit()
