from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


ikb_likes = InlineKeyboardMarkup(row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Показать Лайки',callback_data='Показать Лайки')
        ]
    ])
'''

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

ikb_likes = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👤 Профиль'),
            KeyboardButton(text='❤️ Показать Лайки'),
        ],
    ],
    resize_keyboard = True
)
'''