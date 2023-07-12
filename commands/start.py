from typing import Union

from aiogram import types, Router, Bot
from aiogram.enums import ChatType
from aiogram.filters import Command, CommandObject

from date_base.database import Database
from filters.chat_type_filter import ChatTypeFilter
from paremeters.response_templates import START_MESSAGE



user_start_router = Router()


async def cmd_start(
        message: types.Message,
        command: Union[CommandObject, None],
        db: Database,
        bot: Bot

):
    user = await db.users.get(message.from_user.id)
    if user is None:
        user = await db.users.new(user_id=message.from_user.id,
                                  user_name=message.from_user.username,
                                  first_name=message.from_user.first_name,
                                  second_name=message.from_user.last_name)
    await bot.send_message(text=START_MESSAGE, chat_id=message.from_user.id)


@user_start_router.message(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Command(START_MESSAGE),
    flags={'chat_action': 'typing', 'registrations': False})
async def cmd_start_message(message: types.Message, command: CommandObject, db: Database, bot: Bot):
    await cmd_start(message, command, db, bot)


@user_start_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Command(START_MESSAGE),
    flags={'chat_action': 'typing', 'registrations': False})
async def cmd_start_callback_query(Callback: types.CallbackQuery, command: CommandObject, db: Database, bot: Bot):
    await cmd_start(Callback, None, db, bot)




