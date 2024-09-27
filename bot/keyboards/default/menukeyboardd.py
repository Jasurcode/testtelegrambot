from idlelib.editor import keynames

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Asosiy bolim'),
            KeyboardButton(text='Malumotlar'),
        ],
        [
            KeyboardButton(text="Info"),
            KeyboardButton(text="Aloqa")
        ]
    ]
)