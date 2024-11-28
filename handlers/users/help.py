from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart


router = Router()

@router.message(Command("help"))
@router.message(CommandStart(deep_link=True), F.text.endswith("help"))
async def cmd_help(msg: types.Message):
    await msg.reply(
        text="Help message"
    )
