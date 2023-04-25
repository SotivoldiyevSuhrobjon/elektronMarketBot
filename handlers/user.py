from aiogram import Dispatcher
from aiogram.types import *
from start import dp


async def start_bot_handler(message: Message):
    await message.answer("Salom")


def register_user_py(dp: Dispatcher):
    dp.register_message_handler(start_bot_handler, commands=['start'])
