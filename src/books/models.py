
from sqlmodel import SQLModel,Field, Column
import sqlalchemy.dialects.postgresql as pg 
from datetime import datetime
import uuid
class Book(SQLModel,table = True):
    __tablename__ = "books"
    uid: uuid.UUID = Field(
  sa_column=Column(pg.UUID,   nullable=False  ,primary_key=True , default= uuid.uuid4      )
    )
    title: str
    author: str
    publisher: str
    publisher_date: str
    page_count: int
    language: str
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, nullable=False, default=datetime.now)
    )
    updated_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    )

def __repr__(self):
    return f"<title{self.title}>"
