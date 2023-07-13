from aiogram import Router, types, Bot, F
from aiogram.enums import ChatType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from date_base.models.users import Users
from filters import ChatTypeFilter
from middlewares import RoleMiddleware, BalanceMiddleware
from paremeters.bot_parameters import PARSE_MODE
from paremeters.response_templates import START_RESPONSE
from structures.enums.image import OrderImageGenerate

user_gpt_image_router = Router()

user_gpt_image_router.message.middleware(RoleMiddleware)
user_gpt_image_router.message.middleware(BalanceMiddleware)

@user_gpt_image_router.message(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    OrderImageGenerate.image_generate,
    Command('image')
)
@user_gpt_image_router.message(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    OrderImageGenerate.image_generate,
    F.text,
    flags={'chat_action': 'upload_photo'}
)




async def cmd_image_generate(message: types.Message, state: FSMContext, user: Users, bot: Bot):
    opening_message = await message.answer(START_RESPONSE.format(user.balance),
                                            disable_notification = True,
                                            parse_mode= PARSE_MODE)
    success, response, token = await user_get_image_response(message.from_user.id)

    if success:
        await bot.send_photo(chat_id=message.from_user.id, photo= response)
        await debiting_tokens(user, token)
        await state.clear()

    if not success:
        await bot.send_message(chat_id=message.from_user.id, photo= response)

    await opening_message.delete()