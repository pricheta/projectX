from dependency_injector import containers, providers

from projectX.app.repositories.auth_repository import AuthRepository
from projectX.app.services.auth_service import AuthService
from projectX.connectors.database_engine import get_database_engine
from projectX.infra.database.auth import get_auth_table

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "projectX.app.routers.auth_router",
        ],
    )

    database_engine = providers.Singleton(get_database_engine)
    auth_table = providers.Singleton(get_auth_table)

    auth_repository = providers.Singleton(
        AuthRepository,
        database_engine=database_engine,
        auth_table=auth_table,
    )
    auth_service = providers.Singleton(
        AuthService,
        auth_repository=auth_repository,
    )
