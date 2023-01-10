from typing import Optional

import sqlalchemy as sa


class DbAccess:
    def __init__(
        self,
        backend: str,
        user: Optional[str] = None,
        pwd: Optional[str] = None,
        host: Optional[str] = None,
        database: Optional[str] = None,
        port: Optional[int] = None,
    ):
        self.backend = backend
        self.user = user
        self.pwd = pwd
        self.host = host
        self.database = database
        self.port = port

    def make_connection_str(self):
        """
        Return database connection string
        """
        if self.backend == "sqlite":
            url = """{backend}:///{database}.db"""

        return url.format(
            backend=self.backend,
            user=self.user,
            pwd=self.pwd,
            host=self.host,
            port=self.port,
            database=self.database,
        )

    def return_engine(self):
        """
        Create a sqlalchemy db engine for connection.
        """

        return sa.create_engine(
            self.make_connection_str(), poolclass=sa.pool.NullPool
        )
