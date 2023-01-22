# alembic-sqlalchemy-fastapi-example

### Methods
```
pip install -e .
python -m alembic_sqlalchemy_fastapi_example.services.sqlite
python -m alembic_sqlalchemy_fastapi_example.services.fastapi
pip uninstall alembic-sqlalchemy-fastapi-example -y
```

### Check SQLite Database
```
sqlite3 -nullvalue null
.open database.db
.tables
.schema visitor
select * from visitor limit 5;
```
