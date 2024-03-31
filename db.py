from sqlmodel import SQLModel, create_engine
from model import *

#connection with sqlite
sqlite_file_name = "db_hackathon.db"
sqlite_folder = "sqlite"
sqlite_url = f"sqlite:///{sqlite_folder}/{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)