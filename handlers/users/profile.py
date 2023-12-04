from aiogram import types
from loader import dp
from loader import db

from utils.misc import rate_limit

from keyboards.default import kb_menu

@rate_limit(limit=5)
@dp.message_handler(text='👤 Профиль')
async def command_start(message: types.Message):
    data = db.get_user_data(message.from_user.id)
    photo = open(data[5], 'rb')
    caption = (
        f'<b>{data[2]}</b>, {data[3]}\n'
        f'{data[6]}\n\n'
        f'{data[4]}\n\n')
    await dp.bot.send_photo(message.chat.id, photo,caption=caption,reply_markup=kb_menu)