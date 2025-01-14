from aiogram import F, Router

from middlewares.database import DatabaseMiddleware
from middlewares.throttling import ThrottlingMiddleware

from .start import router as start_router
from .help import router as help_router
from .about import router as about_router
from .unknown import router as unknown_router

user_router = Router(name="User router")

user_router.message.filter(F.text)
user_router.message.filter(F.chat.type == 'private')

user_router.include_router(help_router)
user_router.include_router(start_router)
user_router.include_router(about_router)
# user_router.include_router(unknown_router)

user_router.message.middleware.register(DatabaseMiddleware())
user_router.message.middleware.register(ThrottlingMiddleware())
