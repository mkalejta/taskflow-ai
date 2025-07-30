from app.services.db.db import get_engine_from_settings
from app.models.User import User
from app.models.Task import Task
from app.models.Project import Project
from app.models.Chat import Chat
from app.models.base import Base

def create_tables():
    engine = get_engine_from_settings()
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()