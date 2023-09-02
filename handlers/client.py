from aiogram import types
from aiogram.dispatcher import Dispatcher
from handlers.keyboards.kb_client import START, CHOOSE, GET_PHONE, FORMAT, GROUP, SINGLE, get_kb_days, get_kb_intervals
from core.create_bot import dp, bot
from core.implemented import week_schemas, interval_schemas, user_services, lesson_base_services, week_services
from handlers.utils import get_data_week, get_intervals

data = {}

async def process_start_command(message: types.Message):
    await message.reply(f"Привет!\nЭтот бот поможет тебе записаться на урок!",
                        reply_markup=START)

@dp.callback_query_handler(text='add_user_data')
async def add_user(callback_query: types.CallbackQuery):

    user = user_services.get_one(callback_query)

    if user is not None:
        await bot.send_message(callback_query.from_user.id, 'Вы уже зарегестрированы!', reply_markup=CHOOSE)
    else:
        user_services.create(callback_query)
        await bot.send_message(callback_query.from_user.id, 'Вы успешно зарегестрировались!')
        await bot.send_message(callback_query.from_user.id, "Нужен ваш номер телефона", reply_markup=GET_PHONE)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def add_number(message: types.Message):

    user_services.update(message)

    await bot.send_message(message.from_user.id, "Все данные получены, переходим к выбору занятий", reply_markup=CHOOSE)


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
    global data
    data['lesson_type'] = 'Групповое'
    print(data)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Days for registration", reply_markup=get_kb_days(week_schemas.dump(get_data_week())))


@dp.callback_query_handler(text='choosed_single_lesson')
async def choosed_single_command(callback_query: types.CallbackQuery):
    global data
    data['lesson_type'] = 'Индивидуальное'
    print(data)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Days for registration", reply_markup=get_kb_days(week_schemas.dump(get_data_week())))


@dp.callback_query_handler(text_endswith='choosed_day_for_lesson')
async def choosed_day_for_group_command(callback_query: types.CallbackQuery):
    global data
    data['day'] = callback_query.data.split()[0]
    print(data)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Intervals", reply_markup=get_kb_intervals(interval_schemas.dump(get_intervals(data))))


@dp.callback_query_handler(text_endswith='choosed_day_for_lesson')
async def choosed_day_for_single_command(callback_query: types.CallbackQuery):
    global data
    data['day'] = callback_query.data.split()[0]
    print(data)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Intervals", reply_markup=get_kb_intervals(interval_schemas.dump(get_intervals(data))))


@dp.callback_query_handler(text_endswith='choosed_interval_for_lesson')
async def choosed_interval_for_group_command(callback_query: types.CallbackQuery):
    global data
    data['time'] = callback_query.data.split()[0]
    print(data)
    week_services.take_time(data)
    lesson_base_services.create(data, callback_query)
    data = {}
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы записаны!")


@dp.callback_query_handler(text_endswith='choosed_interval_for_lesson')
async def choosed_interval_for_single_command(callback_query: types.CallbackQuery):
    global data
    data['time'] = callback_query.data.split()[0]
    print(data)
    week_services.take_time(data)
    lesson_base_services.create(data, callback_query)
    data = {}
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы записаны!")

def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
