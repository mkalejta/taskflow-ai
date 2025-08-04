import datetime

from app.projects.schemas import ProjectRequest, ProjectResponse
from app.db.models import User, Project
from fastapi import HTTPException
from sqlalchemy.orm import Session

def convert_project_request(project: ProjectRequest) -> Project:
    """Converts ProjectRequest object to projects object"""
    return Project(**project.dict())


def convert_to_project_response(project: Project, db: Session) -> ProjectResponse:
    """Converts projects object to ProjectResponse object"""
    author = db.query(User).get(project.author_id).full_name()
    return ProjectResponse(
        id=project.id,
        name=project.name,
        description=project.description,
        created_at=project.created_at,
        updated_at=project.updated_at,
        author=author
    )

def get_projects(db: Session) -> list[ProjectResponse]:
    projects = db.query(Project).all()
    return [convert_to_project_response(p, db) for p in projects]


def get_project(id: int, db: Session) -> ProjectResponse:
    project = db.query(Project).get(id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found!")
    return convert_to_project_response(project, db)


def add_project(project: ProjectRequest, db: Session) -> ProjectResponse:
    new_project = convert_project_request(project)
    new_project.created_at = datetime.datetime.now(tz=datetime.timezone.utc)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return convert_to_project_response(new_project, db)


def update_project(id: int, project: ProjectRequest, db: Session) -> ProjectResponse:
    old_project = db.query(Project).get(id)
    if old_project is None:
        raise HTTPException(status_code=404, detail="Project not found!")
    for k, v in project.dict().items():
        setattr(old_project, k, v)
    old_project.updated_at = datetime.datetime.now(tz=datetime.timezone.utc)
    db.commit()
    db.refresh(old_project)
    return convert_to_project_response(old_project, db)


def delete_project(id: int, db: Session) -> str:
    project = db.query(Project).get(id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found!")
    db.delete(project)
    db.commit()
    return 'Project deleted successfully.'