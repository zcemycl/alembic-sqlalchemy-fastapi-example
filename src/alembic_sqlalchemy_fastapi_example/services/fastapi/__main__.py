from typing import List, Optional

from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select

from alembic_sqlalchemy_fastapi_example.definitions.database import DbAccess
from alembic_sqlalchemy_fastapi_example.definitions.dataclasses import Visitor

app = FastAPI()
engine = DbAccess(
    backend="sqlite",
    user="user",
    pwd="1234",
    host="localhost",
    port=6666,
    database="database",
).return_engine()


@app.get("/", status_code=200)
def root() -> dict:
    return {"msg": "Hello, World!"}


@app.get("/visitors/", response_model=List[Visitor])
def read_visits_by_visitor_ip(visitor_ip: str, max_results: Optional[int] = 3):
    with Session(engine) as session:
        statement = (
            select(Visitor).where(Visitor.ip == visitor_ip).limit(max_results)
        )
        visits = session.exec(statement).all()
        if not visits:
            raise HTTPException(
                status_code=404, detail="Visit Records not found."
            )
        return visits


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
