
from typing import Union, Any,Awaitable,Callable,Dict
from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from date_base.database import Database
from structures.data_structures import TransferData, TransferUserData


class DatabaseMiddleware(BaseMiddleware):
    async def __init__(self,
                       handler: Callable[[Message, Dict[str,Any]], Awaitable[Any]],
                       event: Union[Message, CallbackQuery],
                       data: Union[TransferData, TransferUserData],
    ) -> Any:
        async with data.get("pool")() as session:
            data['db'] = Database(session)
            return await handler(event,data)


