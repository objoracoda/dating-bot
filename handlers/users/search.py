from aiogram import types
from loader import dp
from loader import db

from utils.misc import rate_limit

@dp.message_handler(text='🚀 Вперед')
async def command_start(message: types.Message):
    data = db.get_users_recommend('19')[0]
    photo = open(data[5], 'rb')
    caption = (
        f'<b>{data[2]}</b>, {data[3]}\n'
        f'{data[6]}\n\n'
        f'{data[4]}\n\n')
    await dp.bot.send_photo(message.chat.id, photo,caption=caption)
