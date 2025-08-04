from app.projects.schemas import ProjectRequest, ProjectResponse
from app.db.models import User, Project
from fastapi import HTTPException
from sqlalchemy.orm import Session

def convert_project_request(project: ProjectRequest) -> Project:
    """Converts ProjectRequest object to projects object"""
    project_model = Project(**project.dict())
    return project_model


def convert_to_project_response(project: Project, db: Session) -> ProjectResponse:
    """Converts projects object to ProjectResponse object"""
    author = db.query(User).get(project.author_id).full_name()
    return ProjectResponse(
        id=project.id,
        name=project.name,
        description=project.description,
        author=author
    )

def get_projects(db: Session) -> list[ProjectResponse]:
    projects = db.query(Project).all()
    response = [convert_to_project_response(p, db) for p in projects]
    return response


def get_project(id: int, db: Session) -> ProjectResponse:
    project = db.query(Project).get(id)
    if project is None:
        raise HTTPException(status_code=404, detail="projects not found!")
    response = convert_to_project_response(project, db)
    return response


def add_project(project: ProjectRequest, db: Session) -> ProjectResponse:
    new_project = convert_project_request(project)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    response = convert_to_project_response(new_project, db)
    return response


def update_project(project: ProjectRequest, db: Session) -> ProjectResponse:
    new_project = convert_project_request(project)
    old_project = db.query(Project).get(id)
    if old_project is None:
        raise HTTPException(status_code=404, detail="projects not found!")
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    response = convert_to_project_response(new_project, db)
    return response


def delete_project(id: int, db: Session) -> str:
    project = db.query(Project).get(id)
    if project is None:
        raise HTTPException(status_code=404, detail="projects not found!")
    db.delete(project)
    db.commit()
    return 'projects deleted successfully.'