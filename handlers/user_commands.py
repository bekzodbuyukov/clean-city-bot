from bot import dp
from aiogram import types
from aiogram.types import Message
from keyboards import keyboards
from db import db_controller
from localizations.locals import get_string_by_language, get_string
from localizations.strings import choose_language_action_text


async def send_result(string_key_name: str, menu_type: str, message: Message):
    user_id = message.chat.id

    menus = {
        "main_menu": keyboards.get_main_menu(user_id),
        "settings_menu": keyboards.get_settings_menu(user_id),
        "change_language_menu": keyboards.CHANGE_LANGUAGE_MENU
    }

    await message.answer(text=get_string(string_key_name, user_id),
                         reply_markup=menus[menu_type])


# @dp.message_handler(content_types=types.ContentTypes.TEXT)
# async def control_text(message: Message):
#     settings_action = await send_result("settings", "settings_menu", message)
#     home_action = await send_result("home", "main_menu", message)
#     about_action = await send_result("about", "main_menu", message)
#
#     text = {
#         "Sozlammalar": settings_action,
#         "Созламмалар": settings_action,
#         "Настройки": settings_action,
#         "Settings": settings_action,
#         "Bosh bo'lim": home_action,
#         "Бош бўлим": home_action,
#         "Главное меню": home_action,
#         "Main menu": home_action,
#         "Bot haqida": about_action,
#         "Бот ҳақида": about_action,
#         "О боте": about_action,
#         "About bot": about_action
#     }
#
#     text[message.text]

# settings menu for different user languages
@dp.message_handler(text="Sozlammalar")
async def send_settings(message: Message):
    await send_result("settings", "settings_menu", message)


@dp.message_handler(text="Созламмалар")
async def send_settings(message: Message):
    await send_result("settings", "settings_menu", message)


@dp.message_handler(text="Настройки")
async def send_settings(message: Message):
    await send_result("settings", "settings_menu", message)


@dp.message_handler(text="Settings")
async def send_settings(message: Message):
    await send_result("settings", "settings_menu", message)


# home button for different user languages
@dp.message_handler(text="Bosh bo'lim")
async def send_main_menu(message: Message):
    await send_result("home", "main_menu", message)


@dp.message_handler(text="Бош бўлим")
async def send_main_menu(message: Message):
    await send_result("home", "main_menu", message)


@dp.message_handler(text="Главное меню")
async def send_main_menu(message: Message):
    await send_result("home", "main_menu", message)


@dp.message_handler(text="Main menu")
async def send_main_menu(message: Message):
    await send_result("home", "main_menu", message)


# about bot button result for user's different interface languages
@dp.message_handler(text="Bot haqida")
async def send_about(message: Message):
    await send_result("about", "main_menu", message)


@dp.message_handler(text="Бот ҳақида")
async def send_about(message: Message):
     await send_result("about", "main_menu", message)


@dp.message_handler(text="О боте")
async def send_about(message: Message):
    await send_result("about", "main_menu", message)


@dp.message_handler(text="About bot")
async def send_about(message: Message):
    await send_result("about", "main_menu", message)


# button for changing language in different languages
async def call_action(message: Message):
    await message.answer(text=choose_language_action_text, reply_markup=keyboards.CHANGE_LANGUAGE_MENU)


@dp.message_handler(text="Tilni o'zgartirish")
async def change_language(message: Message):
    await call_action(message)


@dp.message_handler(text="Тилни ўзгартириш")
async def change_language(message: Message):
    await call_action(message)


@dp.message_handler(text="Сменить язык")
async def change_language(message: Message):
    await call_action(message)


@dp.message_handler(text="Change language")
async def change_language(message: Message):
    await call_action(message)


# change language action
async def inform_language_changed(message: Message):
    await message.bot.delete_message(message.chat.id, message.message_id)
    await message.answer(text=get_string("can_change_language", message.chat.id),
                         reply_markup=keyboards.get_main_menu(message.chat.id))


# problem button
@dp.message_handler(text="Muammo haqida habar berish")
async def inform_about_problem(message: Message):
    await send_result("problem", "main_menu", message)


@dp.message_handler(text="Муаммо ҳақида ҳабар бериш")
async def inform_about_problem(message: Message):
    await send_result("problem", "main_menu", message)


@dp.message_handler(text="Сообщить о проблеме")
async def inform_about_problem(message: Message):
    await send_result("problem", "main_menu", message)


@dp.message_handler(text="Report a problem")
async def inform_about_problem(message: Message):
    await send_result("problem", "main_menu", message)
