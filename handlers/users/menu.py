from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default import kb_menu
from loader import dp


@dp.message_handler(Command("menu"))
async def menu(message: types.Message):
    '''Тут должно быть отображение анкеты пользователя'''
    await message.answer('Что будем делать?',reply_markup=kb_menu)