from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kb_search_react = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'❤️'),
            KeyboardButton(text=f'💔'),
            KeyboardButton(text=f'💤'),
        ],
    ],
    resize_keyboard = True)