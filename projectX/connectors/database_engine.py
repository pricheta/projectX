import os

from sqlalchemy.engine.base import Engine

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_LOGIN = os.environ.get("DB_LOGIN")
DB_PASSWORD = os.environ.get("DB_PASSWORD")


def get_database_engine() -> Engine :
    return create_engine(f'mysql+mysqlconnector://{DB_LOGIN}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')
