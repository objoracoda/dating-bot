from aiogram import types
from loader import dp

from utils.misc import rate_limit

from keyboards.default import kb_start_reg


@rate_limit(limit=5)
@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    photo = open('media/reg.jpg', 'rb')
    caption = (
        "Я Бот Для Знакомств! 🫦\n\n"
        "Для начала, давай узнаем друг-друга получше 👀\n\n"
        "Помоги мне составить твою анкету 👇")
    await dp.bot.send_photo(message.chat.id, photo,caption=caption,reply_markup=kb_start_reg)