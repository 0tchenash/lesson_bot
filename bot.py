from core.create_bot import dp
from aiogram.utils import executor
from handlers import client




async def on_startup(_):

    print('бот вышел в онлайн')

client.register_handler_client(dp)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
