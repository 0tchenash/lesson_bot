from aiogram import types
from aiogram.dispatcher import Dispatcher
from core.create_bot import dp, bot
from handlers.keyboards.kb_admin import ADMIN
from core.implemented import week_services, week_schemas, interval_services, interval_schemas
from handlers.utils import get_data_week, get_intervals

async def admin_start(message: types.Message):
     await message.reply(f"Привет, админ!",
                        reply_markup=ADMIN)

@dp.callback_query_handler(text='update')
async def update_database(callback_query: types.CallbackQuery):
    week_services.create_all_weekdays()
    await bot.send_message(callback_query.from_user.id, "Все тип-топ", reply_markup=ADMIN)

@dp.callback_query_handler(text='delete')
async def delete_lesson(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Урок удален", reply_markup=ADMIN)

@dp.callback_query_handler(text='check')
async def check_lessons(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Расписание на сегодня", reply_markup=ADMIN)

def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=['admin'])