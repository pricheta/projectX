from dependency_injector.wiring import inject
from fastapi import HTTPException
from sqlalchemy import Table, select
from sqlalchemy.engine.base import Engine
from sqlalchemy.exc import IntegrityError


class AuthRepository:
    @inject
    def __init__(
        self,
        database_engine: Engine,
        auth_table: Table,
    ) -> None:
        self.database_engine = database_engine
        self.auth_table = auth_table

    def register(self, login: str, password: str) -> None:
        query = self.auth_table.insert().values(login=login, password=password)
        try:
            with self.database_engine.connect() as connection:
                connection.execute(query)
                connection.commit()
        except IntegrityError:
            connection.rollback()
            raise HTTPException(status_code=400, detail="Пользователь с указанным логином уже существует.")


    def check_credentials(self, login: str, password: str) -> bool:
        query = select(self.auth_table).filter(self.auth_table.c.login == login, self.auth_table.c.password == password)
        with self.database_engine.connect() as connection:
            response = connection.execute(query).fetchall()
        return bool(response)
