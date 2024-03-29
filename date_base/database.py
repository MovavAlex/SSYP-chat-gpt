from typing import Union

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.orm import sessionmaker

from date_base.repositories.users import UserRepo
from date_base.repositories.promo_codes import PromoCodeRepo
from date_base.repositories.used_promo_codes import UsedPromoRepo


def create_async_engine(url: Union[URL, str]) -> AsyncEngine:
    """ Create async engine """
    return _create_async_engine(url=url,
                                echo=False,
                                pool_pre_ping=True
                                )
def create_session_maker(engine: AsyncEngine = None) -> sessionmaker:
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

    users: UserRepo

    promo_codes: PromoCodeRepo

    used_promo_code: UsedPromoRepo

    sesion: AsyncSession

def __init__(
        self,
        session:AsyncSession,
        user: UserRepo = None,
        promo_code: PromoCodeRepo = None,
        used_promo_code: UsedPromoRepo = None

):
    self.session = session
    self.user = user or UserRepo(session=session)
    self.promo_codes = promo_code or PromoCodeRepo(session=session)
    self.used_promo_codes = used_promo_code or UsedPromoRepo(session=session)



















