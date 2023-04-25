from aiogram import Bot, Dispatcher, executor, types
import logging
from config import BOT_TOKEN

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from handlers.user import register_user_py

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)




async def on_startup(dispatcher: Dispatcher):
    register_user_py(dispatcher)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
