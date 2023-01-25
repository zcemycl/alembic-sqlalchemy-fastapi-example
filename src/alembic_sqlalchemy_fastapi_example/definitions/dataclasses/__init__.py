from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Index, Relationship, SQLModel, UniqueConstraint


class Topic(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("name", "version"),
        Index("idx_topic_version", "name", "version"),
    )
    id: Optional[int] = Field(default=None, primary_key=True)
    version: str  # vx.x.x
    name: str = Field(index=True)
    visitors: List["Visitor"] = Relationship(back_populates="topic")
    last_modified_at: datetime = Field(default_factory=datetime.utcnow)


class InternetProtocol(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("address", "lat", "lng", "country", "timestamp"),
        Index("idx_lat_lng", "lat", "lng"),
    )
    id: Optional[int] = Field(default=None, primary_key=True)
    address: str = Field(index=True)
    lat: float
    lng: float
    country: str = Field(index=True)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    visitors: List["Visitor"] = Relationship(back_populates="ip")


class Visitor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ip_id: Optional[int] = Field(foreign_key="internetprotocol.id", index=True)
    ip: Optional[InternetProtocol] = Relationship(back_populates="visitors")
    topic_id: Optional[int] = Field(foreign_key="topic.id", index=True)
    topic: Optional[Topic] = Relationship(back_populates="visitors")
    created_at: datetime = Field(default_factory=datetime.utcnow)
