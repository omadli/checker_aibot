from aiogram import Dispatcher

from handlers.admins import admin_router
from handlers.users import user_router


def include_all_routers(dp: Dispatcher):
    dp.include_router(admin_router)
    dp.include_router(user_router)
