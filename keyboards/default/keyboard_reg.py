from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kb_reg = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👤 Профиль'),
        ],
    ],
    resize_keyboard = True
)