from app.projects.schemas import ProjectRequest, ProjectResponse
from app.db.models import User, Project
from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload


def convert_to_project_response(project: Project, db: Session) -> ProjectResponse:
    """Converts projects object to ProjectResponse object"""
    return ProjectResponse.from_orm(project).copy(update={"author": db.query(User).get(project.author_id).full_name()})


def get_projects(db: Session) -> list[ProjectResponse]:
    projects = db.query(Project).options(joinedload(Project.author)).all()  # automatic data attachment from 'users' table to sent less request to db
    return [ProjectResponse.from_orm(p).copy(update={"author": p.author.full_name()}) for p in projects]


def get_project(id: int, db: Session) -> ProjectResponse:
    project = db.query(Project).get(id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found!")
    return convert_to_project_response(project, db)


def add_project(project: ProjectRequest, db: Session) -> ProjectResponse:
    new_project = Project(**project.dict())
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
    db.commit()
    db.refresh(old_project)
    return convert_to_project_response(old_project, db)


def delete_project(id: int, db: Session) -> None:
    project = db.query(Project).get(id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found!")
    db.delete(project)
    db.commit()
    return None