from aiogram import types
from loader import dp

from loader import db

@dp.message_handler(text='/help')
async def command_help(message: types.Message):
    exist = db.user_exists(message.from_user.id)
    await message.answer(f'Привет! {message.from_user.full_name}!\n'
    f'{exist}')