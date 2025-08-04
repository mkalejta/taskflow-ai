from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.projects.schemas import ProjectResponse, ProjectRequest
import app.projects.services as ps

router = APIRouter()

@router.get('/', response_model=list[ProjectResponse])
async def read_projects(db: Session = Depends(get_db)):
    return ps.get_projects(db)

@router.post('/', response_model=ProjectResponse)
async def create_project(project: ProjectRequest, db: Session = Depends(get_db)):
    return ps.add_project(project, db)

@router.get('/{project_id}', response_model=ProjectResponse)
async def read_project(project_id: int, db: Session = Depends(get_db)):
    return ps.get_project(project_id, db)

@router.put('/{project_id}', response_model=ProjectResponse)
async def update_project(project_id: int, project: ProjectRequest, db: Session = Depends(get_db)):
    return ps.update_project(project_id, project, db)

@router.delete('/{project_id}', status_code=204)
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    return ps.delete_project(project_id, db)