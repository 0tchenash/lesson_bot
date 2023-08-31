from aiogram import Bot, Dispatcher
from core.config import API_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot, storage=storage)
