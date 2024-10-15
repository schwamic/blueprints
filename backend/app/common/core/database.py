from sqlmodel import (
    Session,
    create_engine
)
from pydantic_core import MultiHostUrl
from .settings import settings

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

postgres_url = MultiHostUrl.build(
    scheme="postgresql+psycopg",
    username=settings.POSTGRES.user,
    password=settings.POSTGRES.password,
    host=settings.POSTGRES.server,
    port=settings.POSTGRES.port,
    path=settings.POSTGRES.db,
)

connect_args = {"check_same_thread": False}
engine = create_engine(postgres_url, echo=True, connect_args=connect_args)

def init_db(session: Session) -> None:
    # Tables will be created with Alembic
    pass
