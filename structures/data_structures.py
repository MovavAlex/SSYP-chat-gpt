
from typing import Callable, TypedDict

from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncSession

from structures.enum.role import Role
from cache import Cache
from data_base import Database

class TransferData(TypedDict):
    pool: Callable[[], AsyncSession]
    db: Database
    bot: Bot
    #cache: Cache

class TransferUserData(TypedDict):
    role: Role
