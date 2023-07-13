from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats

from commands.commandName import START_COMMAND, RESET_COMMAND, CANCEL_COMMAND, REPLY_COMMAND
async def set_bot_commands(self, Bot):
    data = [
        {
            [
                BotCommand(commands=START_COMMAND, description='Регистрация'),
                BotCommand(command=RESET_COMMAND, description='Очиещение чата'),
                BotCommand(commands=CANCEL_COMMAND, description='Остановка чата'),
                BotCommand(commands=REPLY_COMMAND, description='Повторить комманду'),
                BotCommand(commands=IMAGE_COMMAND, description='Сгенерировать изображение'),

            ],
            BotCommandScopeAllPrivateChats(),
            None
        }

    ]
    for commands_list(), command_scope, language in data:
        await bot.set_my_commands(commands= commands_list(), scope=command_scope, language_code=language
                                  )
