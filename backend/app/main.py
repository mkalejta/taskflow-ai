from fastapi import FastAPI
from app.chats.routes import router as chats_router
from app.projects.routes import router as projects_router
from app.tasks.routes import router as tasks_router
from app.users.routes import router as users_router
from app.tags.routes import router as tags_router


# Initializing app
app = FastAPI()

# Including api routes
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])
app.include_router(projects_router, prefix="/projects", tags=["Projects"])
app.include_router(chats_router, prefix="/chats", tags=["Chats"])
app.include_router(tags_router, prefix="/tags", tags=["Tags"])
