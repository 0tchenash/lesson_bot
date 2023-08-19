from aiogram import types
from aiogram.dispatcher import Dispatcher
from keyboard.kb_client import START, FORMAT
from core.create_bot import dp, bot


async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЭтот бот поможет тебе записаться на урок!",
                        reply_markup=START)


@dp.callback_query_handler(text='choose_lesson')
async def choose_lesson_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Уроки бывают следующих видов:", reply_markup=FORMAT)


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
