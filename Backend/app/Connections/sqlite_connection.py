from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os
sqlite_file = "app/Connections/Entry.db"
sqlite_url = f"sqlite:///{sqlite_file}"
engine = create_engine(sqlite_url, echo=True)

def initialize_bd():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)