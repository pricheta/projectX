from sqlalchemy import MetaData, Table, Column, String


metadata = MetaData()

def get_auth_table() -> Table:
    return Table(
    'auth',
    metadata,
    Column('login', String(20), primary_key=True, nullable=False),
    Column('password', String(60), nullable=False),
)
