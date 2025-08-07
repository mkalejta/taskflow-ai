from app.projects.schemas import ProjectRequest, ProjectResponse
from app.db.models import Project
from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from app.tasks.services import convert_task_to_response


def convert_to_project_response(project: Project) -> ProjectResponse:
    """Converts projects object to ProjectResponse object"""
    project_dict = {
        "id": project.id,
        "author": project.author.full_name,
        "name": project.name,
        "description": project.description,
        "created_at": project.created_at,
        "updated_at": project.updated_at,
        "tasks": [convert_task_to_response(t) for t in project.tasks]
    }
    return ProjectResponse(**project_dict)


def get_projects(db: Session) -> list[ProjectResponse]:
    projects = db.query(Project).options(joinedload(Project.author)).all()  # automatic data attachment from 'users' table to sent less request to db
    return [convert_to_project_response(p) for p in projects]


def get_project(id: int, db: Session) -> ProjectResponse:
    project = db.get(Project, id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found!")
    return convert_to_project_response(project)


def add_project(project: ProjectRequest, db: Session) -> ProjectResponse:
    new_project = Project(**project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return convert_to_project_response(new_project)


def update_project(id: int, project: ProjectRequest, db: Session) -> ProjectResponse:
    old_project = db.get(Project, id)
    if old_project is None:
        raise HTTPException(status_code=404, detail="Project not found!")
    for k, v in project.dict(exclude={'author_id'}).items():
        setattr(old_project, k, v)
    db.commit()
    db.refresh(old_project)
    return convert_to_project_response(old_project)


def delete_project(id: int, db: Session) -> None:
    project = db.get(Project, id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found!")
    db.delete(project)
    db.commit()