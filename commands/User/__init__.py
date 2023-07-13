from aiogram import Router
from middlewares.middleware import DatabaseMiddleware
from middlewares.users import UserMiddleware
from commands.start import user_start_router
from commands.User.gpt_image import user_gpt_image_router
user_router = Router(name='user')

user_router.message.middleware(DatabaseMiddleware())
user_router.message.middleware(UserMiddleware())

user_router.callback_query.middleware(DatabaseMiddleware())
user_router.callback_query.middleware(UserMiddleware())


user_router.include_router(user_start_router, user_gpt_image_router)