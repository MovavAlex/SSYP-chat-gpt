from aiogram import types
from aiogram.filters import Text, Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import openai
import logging

import asyncio
from aiogram import Bot, Dispatcher

from paremeters.chat_gpt_paremeters import TELEGRAM_TOKEN, CHAT_GPT_KEY
from date_base.database import create_session_maker
from structures.data_structures import TransferData
from structures import conf, set_bot_commands, Role


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

messages = [
    {
        'role': 'user',
     'content': 'Привет'
    }
            ]

max_token_count = 200

def update(messages, role, content):
    messages.append({'role':role,'content':content})


def reset_messages(messages):
    messages.clear()
    messages.append({'role': 'user', 'content': 'Привет'})



async def main():
    await dp.start_polling(bot)


@dp.message_handler(Command("start"))
async def start_bot(message: types.Message):
    buttons = InlineKeyboardButton(text="Пополнить баланс", callback_data="Start")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[buttons]])
    await message.answer("Выберите функцию или начните общение", reply_markup=keyboard)


@dp.callback_query_handler(Text("Start"))
async def start_bot(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Функционала пока нет(')



@dp.message_handler()
async def send(message: types.Message):
    update(messages, 'user', message.text)
    response = openai.ChatCompletion.create(
        CHAT_GPT_KEY,
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=max_token_count,
        )
    if response['usage']['total_tokens'] >= max_token_count:
        reset_messages(messages)
    await message.answer(response['choices'][0]['message']['content'], parse_mode="markdown")



@dp.message_handler(Command('help'))
async def help(message: types.Message):
    await message.answer('Список комманд для бота: /reset - очищает историю сообщений')


@dp.message_handler(Command('reset'))
async def reset(message: types.Message):
    reset_messages(messages)
    print(messages)
    await message.answer('История сообщений сброшена')



logger = logging.getLogger(__name__)

async def start_bot():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s]'u' - %(name)s - %(message)s',
        file_name='.../bot_history'
    )
    logger.info('starting_bot')

    bot= Bot(token=conf.bot.token)

    transfer_data: TransferData = TransferData(pool= create_session_maker())

    await set_bot_command(bot)

    try:
        await dp.start_polling(
            bot,
            allowed_update= dp.resolve_used_update_types(),
            **transfer_data)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(start_bot)
    except {KeyboardInterrupt, SystemError}:
        logger.error('Bot stopped')











# async def cmd_random(message: types.Message):
#     button = InlineKeyboardButton(text="начать игру", callback_data="random")
#     keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
#     await message.answer("Нажми на кнопку", reply_markup=keyboard)
#
#
# @dp.callback_query(Text("random"))
# async def cmd_random(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id, text=str(randint(0, 10)))
#











if __name__ == "__main__":
    asyncio.run(main())
