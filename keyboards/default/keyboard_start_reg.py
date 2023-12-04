from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kb_start_reg = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'👤 Новая Анкета'),
        ],
    ],
    resize_keyboard = True)