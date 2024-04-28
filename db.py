from sqlalchemy import create_engine
from model_2 import Base

#connection with sqlite
#sqlite_file_name = "db_hackathon.db"
sqlite_file_name = "db_test.db"
sqlite_folder = "sqlite"
sqlite_url = f"sqlite:///{sqlite_folder}/{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    Base.metadata.create_all(engine)