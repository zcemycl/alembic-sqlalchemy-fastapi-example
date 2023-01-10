from typing import Optional

from sqlmodel import Field, SQLModel


class Visitor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ip: str
    topic: str
