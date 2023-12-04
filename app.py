async def on_startup(dp):
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    import middlewares
    middlewares.setup(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print('Starting Bot...')


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

'''
import os
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InputFile
from aiogram.types.message import ContentType

import data.config as cfg


#TELEGRAM_API_TOKEN = os.getenv('MY_TELEGRAM_TOKEN', 'Token Not found')
TELEGRAM_API_TOKEN = cfg.token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)

#db = Database('database.db')


@dp.message_handler(commands=["start"])
async def welcome_msg(message: types.Message):
    #db.add_user(message.from_user.id)
    #photo = open('reg.jpg', 'rb')
    caption = (
        "Я Бот Для Знакомств! 🫦\n\n"
        "Для начала, давай познакомимся 👀\n\n"
        "Как тебя зовут?")
    #await bot.send_photo(message.chat.id, photo,caption=caption)
    await bot.send_message(message.from_user.id, "Привет!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)'''