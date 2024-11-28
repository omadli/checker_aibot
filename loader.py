from aiogram import Dispatcher, Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from settings import BOT_TOKEN


bot = Bot(
    token=BOT_TOKEN, 
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
        allow_sending_without_reply=True,
    )
)
dp = Dispatcher(
    storage=MemoryStorage()
)
