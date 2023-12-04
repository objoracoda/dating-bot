from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🚀 Вперед'),
            KeyboardButton(text='🌹 Подписка'),
        ],
        [
            KeyboardButton(text='👤 Новая Анкета'),
        ]
    ],
    resize_keyboard = True
)