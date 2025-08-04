from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database
from app.settings import postgres as settings


def get_engine(user, password, host, port, db):
    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine


def get_engine_from_settings():
    keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb']
    if not all(key in keys for key in settings.keys()):
        raise Exception('Bad config settings')

    return get_engine(settings['pguser'], settings['pgpasswd'], settings['pghost'], settings['pgport'], settings['pgdb'])


engine = get_engine_from_settings()
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()