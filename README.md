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

### Interesting Questions
1. How to do database migration easily?
    - Adding new columns
    - Adding new indices
    - Overall redesign of database schemas
        - If so, backfill?
2. How to design an user-post-comment-record relationship?
3. Can we do ab-testing for frontend?

### References
1. [In-Depth Guide to Backend Route Design](https://softgrade.org/in-depth-guide-to-backend-route-design/)
2. [Best practices for REST API design](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
3. [Relationship back_populates](https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/back-populates/)
4. [Hyperproductive API clients with FastAPI using OpenAPI Generator](https://gaganpreet.in/posts/hyperproductive-apis-fastapi/)
5. [OpenAPI and CodeGen](https://medium.com/@almondcrush/openapi-and-codegen-e275e199ef13)
