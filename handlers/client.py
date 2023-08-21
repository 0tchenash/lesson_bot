from aiogram import types
from aiogram.dispatcher import Dispatcher
from keyboard.kb_client import START, FORMAT, GROUP, SINGLE, DAYS
from core.create_bot import dp, bot
from core.implemented import week_services

async def process_start_command(message: types.Message):
    week_services.sorted_data_week()
    await message.reply("Привет!\nЭтот бот поможет тебе записаться на урок!",
                        reply_markup=START)


@dp.callback_query_handler(text='choose_lesson')
async def choose_lesson_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Уроки бывают следующих видов:", reply_markup=FORMAT)


@dp.callback_query_handler(text='single_lesson')
async def choose_single_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Description of single lesson", reply_markup=SINGLE)


@dp.callback_query_handler(text='group_lesson')
async def choose_group_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Description of group lesson", reply_markup=GROUP)


@dp.callback_query_handler(text='choosed_group_lesson')
async def choosed_group_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Days for registration", reply_markup=DAYS)


@dp.callback_query_handler(text='choosed_single_lesson')
async def choosed_single_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Days for registration", reply_markup=DAYS)


@dp.message_handler(commands='choosed_group_lesson')
async def choosed_day_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Days for registration", reply_markup=DAYS)


@dp.callback_query_handler(text='choosed_single_lesson')
async def choosed_single_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Days for registration", reply_markup=DAYS)


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
