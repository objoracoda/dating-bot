from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kb_city = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Москва'),
        ],
    ],
    resize_keyboard = True
)