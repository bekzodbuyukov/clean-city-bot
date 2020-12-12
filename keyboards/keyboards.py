from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from handlers import callback  # this import must be here


MAIN_MENU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Muammo haqida habar berish")
        ],
        [
            KeyboardButton(text="Bot haqida"),
            KeyboardButton(text="Sozlammalar")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

CHOOSE_LANGUAGE_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbekcha", callback_data="oz_lang")
        ],
        [
            InlineKeyboardButton(text="Узбекча", callback_data="uz_lang")
        ],
        [
            InlineKeyboardButton(text="Русский язык", callback_data="ru_lang")
        ],
        [
            InlineKeyboardButton(text="English", callback_data="en_lang")
        ]
    ]
)

SHARE_CONTACT_MENU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqamni jo'natish", request_contact=True)
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
