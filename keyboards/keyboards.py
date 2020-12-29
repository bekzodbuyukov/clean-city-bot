from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from handlers import callback  # this import must be here
from localizations.locals import get_string


def get_main_menu(user_id):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=get_string("problem_button", user_id))
            ],
            [
                KeyboardButton(text=get_string("about_button", user_id)),
                KeyboardButton(text=get_string("settings_button", user_id))
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
            InlineKeyboardButton(text="Ўзбекча", callback_data="uz_lang")
        ],
        [
            InlineKeyboardButton(text="Русский язык", callback_data="ru_lang")
        ],
        [
            InlineKeyboardButton(text="English", callback_data="en_lang")
        ]
    ]
)


CHANGE_LANGUAGE_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbekcha", callback_data="to_oz_lang")
        ],
        [
            InlineKeyboardButton(text="Ўзбекча", callback_data="to_uz_lang")
        ],
        [
            InlineKeyboardButton(text="Русский язык", callback_data="to_ru_lang")
        ],
        [
            InlineKeyboardButton(text="English", callback_data="to_en_lang")
        ]
    ]
)


def get_stay_anonymous_menu(user_id):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=get_string("yes_button", user_id)),
                KeyboardButton(text=get_string("no_button", user_id))
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )


def get_share_number_menu(user_id):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=get_string("share_phone_number_button", user_id),
                               request_contact=True)
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )


def get_settings_menu(user_id):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=get_string("change_language_button", user_id)),
            ],
            [
                KeyboardButton(text=get_string("home_button", user_id)),
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )