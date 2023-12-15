from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kb_match_react = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'❤️'),
            KeyboardButton(text=f'💔'),
        ],
    ],
    resize_keyboard = True)