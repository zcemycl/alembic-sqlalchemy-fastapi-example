import datetime
from types import TracebackType
from typing import Optional, Type

from fastapi.testclient import TestClient
from pydantic import BaseModel
from pytest_mock import MockFixture

from alembic_sqlalchemy_fastapi_example.services.fastapi.__main__ import app

client = TestClient(app)


class mockSession:
    def __init__(self, engine, return_values):
        self.engine = engine
        self.return_values = return_values

    def __enter__(self) -> object:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ):
        pass

    def exec(self, query):
        return self

    def all(self):
        return self.return_values


class MVisitor(BaseModel):
    address: str
    version: str
    country: str
    name: str
    created_at: datetime.datetime


def test_read_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"msg": "Hello, World!"}


def test_visitors_404(mocker: MockFixture):
    mocker.patch(
        "alembic_sqlalchemy_fastapi_example.services.fastapi.__main__.engine",
        return_value=None,
    )
    mocker.patch(
        "alembic_sqlalchemy_fastapi_example.services.fastapi.__main__.Session",
        return_value=mockSession(None, []),
    )
    resp = client.get("/visitors/?visitor_ip=206.206.2.2")
    assert resp.status_code == 404


def test_visitors_200(mocker: MockFixture):
    record = [
        {
            "address": "220.246.206.4",
            "country": "United Kingdown",
            "name": "Knowledge Graph",
            "version": "v0.0.0",
            "created_at": "2023-01-25T14:53:17.933427",
        }
    ]
    mocker.patch(
        "alembic_sqlalchemy_fastapi_example.services.fastapi.__main__.engine",
        return_value=None,
    )
    mocker.patch(
        "alembic_sqlalchemy_fastapi_example.services.fastapi.__main__.Session",
        return_value=mockSession(None, record),
    )
    resp = client.get("/visitors/?visitor_ip=206.206.2.4")
    print(resp.json())
    assert resp.status_code == 200
    assert MVisitor.parse_obj(resp.json()[0])
