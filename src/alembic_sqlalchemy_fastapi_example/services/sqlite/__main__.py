from sqlmodel import Session, SQLModel, select

from alembic_sqlalchemy_fastapi_example.definitions.database import DbAccess
from alembic_sqlalchemy_fastapi_example.definitions.dataclasses import (
    InternetProtocol,
    Topic,
    Visitor,
)

engine = DbAccess(
    backend="sqlite",
    user="user",
    pwd="1234",
    host="localhost",
    port=6666,
    database="database",
).return_engine()

SQLModel.metadata.create_all(
    engine,
    tables=[
        SQLModel.metadata.tables["visitor"],
        SQLModel.metadata.tables["topic"],
        SQLModel.metadata.tables["internetprotocol"],
    ],
)

data_topics = [
    {"topic": "Knowledge Graph", "version": "v0.0.0"},
    {"topic": "Chatapp", "version": "v0.0.0"},
    {"topic": "Game", "version": "v0.0.0"},
]

data_visits = [
    {
        "address": "220.246.206.4",
        "lat": 51.477,
        "lng": -0.1959,
        "topic": "Knowledge Graph",
        "version": "v0.0.0",
        "country": "United Kingdown",
    },
    {
        "address": "220.246.206.4",
        "lat": 51.477,
        "lng": -0.1959,
        "topic": "Chatapp",
        "version": "v0.0.0",
        "country": "United Kingdown",
    },
    {
        "address": "220.246.206.4",
        "lat": 22.2908,
        "lng": 114.1501,
        "topic": "Game",
        "version": "v0.0.0",
        "country": "Hong Kong",
    },
    {
        "address": "2.137.82.181",
        "lat": 51.477,
        "lng": -0.1959,
        "topic": "Game",
        "version": "v0.0.0",
        "country": "United Kingdown",
    },
]


def retrieve_topic_history(name: str, version: str):
    content_query = select(Topic).where(
        (Topic.name == name) & (Topic.version == version)
    )
    record = session.execute(content_query).first()
    return record


def retrieve_ip_history(address: str, lat: float, lng: float, country: str):
    ip_query = select(InternetProtocol).where(
        (InternetProtocol.address == address)
        & (InternetProtocol.lat == lat)
        & (InternetProtocol.lng == lng)
        & (InternetProtocol.country == country)
    )

    record = session.execute(ip_query).first()
    return record


with Session(engine) as session:
    for data_topic in data_topics:
        existing_topic = retrieve_topic_history(
            data_topic["topic"], data_topic["version"]
        )
        print(existing_topic)
        if not existing_topic:
            session.add(
                Topic(name=data_topic["topic"], version=data_topic["version"])
            )
    session.commit()

    for data_visit in data_visits:
        existing_ip = retrieve_ip_history(
            data_visit["address"],
            data_visit["lat"],
            data_visit["lng"],
            data_visit["country"],
        )
        print(existing_ip)
        if not existing_ip:
            tmp_ip = InternetProtocol(
                address=data_visit["address"],
                lat=data_visit["lat"],
                lng=data_visit["lng"],
                country=data_visit["country"],
            )
            session.add(tmp_ip)
            existing_ip = [tmp_ip]
        session.commit()
        existing_topic = retrieve_topic_history(
            data_visit["topic"], data_visit["version"]
        )
        print(existing_ip[0], existing_topic[0])
        visit_record = Visitor(ip=existing_ip[0], topic=existing_topic[0])
        session.add(visit_record)
    session.commit()
