from fastapi import FastAPI
from app.schemas.Chat import ChatMessage

app = FastAPI()

chat = "/chats"
project = "/projects"
task = "/tasks"
user = "/users"

@app.get(chat)
async def read_chats():
    return {"message": "List of chats"}

@app.post(chat)
async def create_chat(chat_message: ChatMessage):
    return chat_message

@app.get(f"{chat}/{{chat_id}}")
async def read_chat(chat_id: int):
    return {"message": f"Details of chat {chat_id}"}

@app.put(f"{chat}/{{chat_id}}")
async def update_chat(chat_id: int, chat_message: ChatMessage):
    return {"message": f"Chat {chat_id} updated", "chat": chat_message}

@app.delete(f"{chat}/{{chat_id}}")
async def delete_chat(chat_id: int):
    return {"message": f"Chat {chat_id} deleted"}

#############################################################

@app.get(project)
async def read_projects():
    return {"message": "List of projects"}

@app.post(project)
async def create_project(project: dict):
    return {"message": "Project created", "project": project}

@app.get(f"{project}/{{project_id}}")
async def read_project(project_id: int):
    return {"message": f"Details of project {project_id}"}

@app.put(f"{project}/{{project_id}}")
async def update_project(project_id: int, project: dict):
    return {"message": f"Project {project_id} updated", "project": project}

@app.delete(f"{project}/{{project_id}}")
async def delete_project(project_id: int):
    return {"message": f"Project {project_id} deleted"}

#############################################################

@app.get(task)
async def read_tasks():
    return {"message": "List of tasks"}

@app.post(task)
async def create_task(task: dict):
    return {"message": "Task created", "task": task}

@app.get(f"{task}/{{task_id}}")
async def read_task(task_id: int):
    return {"message": f"Details of task {task_id}"}

@app.put(f"{task}/{{task_id}}")
async def update_task(task_id: int, task: dict):
    return {"message": f"Task {task_id} updated", "task": task}

@app.delete(f"{task}/{{task_id}}")
async def delete_task(task_id: int):
    return {"message": f"Task {task_id} deleted"}

#############################################################

@app.get(user)
async def read_users():
    return {"message": "List of users"}

@app.post(user)
async def create_user(user: dict):
    return {"message": "User created", "user": user}

@app.get(f"{user}/{{user_id}}")
async def read_user(user_id: int):
    return {"message": f"Details of user {user_id}"}

@app.put(f"{user}/{{user_id}}")
async def update_user(user_id: int, user: dict):
    return {"message": f"User {user_id} updated", "user": user}

@app.delete(f"{user}/{{user_id}}")
async def delete_user(user_id: int):
    return {"message": f"User {user_id} deleted"}

