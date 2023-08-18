
import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import executor

API_TOKEN = '6478090484:AAExiij8eJPTqtqkYj5zMo0ZS_cZ4-YEAew'
ADMIN_ID = 1334535476

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
