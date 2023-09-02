from aiogram import types
from aiogram.dispatcher import Dispatcher
from core.create_bot import dp, bot
from core.config import ADMIN_ID
from handlers.keyboards.kb_admin import ADMIN
from core.implemented import week_services, week_schemas, interval_services, interval_schemas, lesson_services
from handlers.utils import get_data_week, get_intervals

async def admin_start(message: types.Message):
    if message.from_user.id == int(ADMIN_ID):
        await message.reply(f"Привет, админ!",
                        reply_markup=ADMIN)
    else: await bot.send_message(message.from_user.id, "Упс! Кажется, вы не админ!")

@dp.callback_query_handler(text='update')
async def update_database(callback_query: types.CallbackQuery):
    data = week_services.get_all_weekdays()
    if data:
        await bot.send_message(callback_query.from_user.id, "Данные уже на месте", reply_markup=ADMIN)
    else:
        week_services.create_all_weekdays()
        lesson_services.create_all_lessons()
        await bot.send_message(callback_query.from_user.id, "Все тип-топ", reply_markup=ADMIN)

@dp.callback_query_handler(text='delete')
async def delete_lesson(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Урок удален", reply_markup=ADMIN)

@dp.callback_query_handler(text='check')
async def check_lessons(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Расписание на сегодня", reply_markup=ADMIN)

def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=['admin'])