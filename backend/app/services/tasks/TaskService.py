from app.models.Task import Task
from app.services.db.db import get_session

session = get_session()

def convert_task(task: Task):
    """Converts task to TaskResponse form"""
    pass


def get_all_tasks():
    return session.query(Task).all()


def get_task(id: int):
    pass


def add_task(task: Task):
    pass


def update_task(task: Task):
    pass


def delete_task(id: int):
    pass


print(get_all_tasks())