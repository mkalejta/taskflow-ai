from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def read_tasks():
    return {"message": "List of tasks"}

@router.post('/')
async def create_task(task: dict):
    return {"message": "Task created", "task": task}

@router.get('/{task_id}')
async def read_task(task_id: int):
    return {"message": f"Details of task {task_id}"}

@router.put('/{task_id}')
async def update_task(task_id: int, task: dict):
    return {"message": f"Task {task_id} updated", "task": task}

@router.delete('/{task_id}')
async def delete_task(task_id: int):
    return {"message": f"Task {task_id} deleted"}