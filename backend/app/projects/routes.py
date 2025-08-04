from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
import app.projects.services as ps


router = APIRouter()

@router.get('/')
async def read_projects(db: Session = Depends(get_db)):
    return ps.get_projects(db=db)

@router.post('/')
async def create_project(project: dict):
    return {"message": "projects created", "projects": project}

@router.get('/{project_id}')
async def read_project(project_id: int):
    return {"message": f"Details of projects {project_id}"}

@router.put('/{project_id}')
async def update_project(project_id: int, project: dict):
    return {"message": f"projects {project_id} updated", "projects": project}

@router.delete('/{project_id}')
async def delete_project(project_id: int):
    return {"message": f"projects {project_id} deleted"}