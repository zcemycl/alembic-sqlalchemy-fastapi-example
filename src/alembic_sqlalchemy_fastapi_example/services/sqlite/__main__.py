from sqlmodel import Session, SQLModel, select

from alembic_sqlalchemy_fastapi_example.definitions.database import DbAccess
from alembic_sqlalchemy_fastapi_example.definitions.dataclasses import Visitor

engine = DbAccess(backend="sqlite", database="database").return_engine()

SQLModel.metadata.create_all(engine)

visit_1 = Visitor(ip="220.246.206.4", topic="Knowledge Graph")
visit_2 = Visitor(ip="220.246.206.4", topic="Chatapp")
visit_3 = Visitor(ip="220.246.206.4", topic="Game")
visit_4 = Visitor(ip="2.137.82.181", topic="Game")


with Session(engine) as session:
    session.add(visit_1)
    session.add(visit_2)
    session.add(visit_3)
    session.add(visit_4)
    session.commit()

    stat = select(Visitor).where(Visitor.ip == "220.246.206.4")
    visits = session.exec(stat).all()
    print(visits)
