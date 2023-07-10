from typing import Union

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.orm import sessionmaker


def create_async_engine(url: Union[URL, str]) -> AsyncEngine:
    """ Create async engine """
    return _create_async_engine(url=url,
                                echo=False,
                                pool_pre_ping=True
                                )
def creatr_session_maker(engine: AsyncEngine = None) -> sessionmaker:
    """
    Create session maker
    :param engine: async engine
    :return:
    """
    return sessionmaker(
        engine or create_async_engine(),
        class_=AsyncSession,
        expire_on_commit=False

)

class Database:
    """
    Database class is the highest abstractions level of database and
    can be used in the commands or any other bot-side functions
    """


