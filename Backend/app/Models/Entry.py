from sqlmodel import SQLModel, Field
from typing import Optional

class Entry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    question: str
    answer: str
    vector: Optional[str] = Field(default=None)
