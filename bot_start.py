from aiogram import types
from aiogram.filters import Text, Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import openai


import asyncio
from aiogram import Bot, Dispatcher

from Project.paremeters.gpt_paremeters import TELEGRAM_TOKEN, CHAT_GPT_KEY

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

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


@dp.message(Command("start"))
async def start_bot(message: types.Message):
    buttons = InlineKeyboardButton(text="Пополнить баланс", callback_data="Start")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[buttons]])
    await message.answer("Выберите функцию или начните общение", reply_markup=keyboard)


@dp.callback_query(Text("Start"))
async def start_bot(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Функционала пока нет(')



@dp.message()
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



@dp.message(Command('help'))
async def help(message: types.Message):
    await bot.send_message('Список комманд для бота: /reset - очищает историю сообщений')


@dp.message(Command('reset'))
async def reset(message: types.Message):
    reset_messages(messages)
    print(messages)
    await message.answer('История сообщений сброшена')























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
