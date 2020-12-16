from bot import dp
from aiogram import types
from aiogram.types import Message
from keyboards import keyboards
from db import db_controller
from localizations.locals import get_string_by_language, get_string
from localizations.strings import choose_language_action_text


# settings menu for different user languages
@dp.message_handler(text="Sozlammalar")
async def send_settings(message: Message):
    await message.answer(text=get_string_by_language("settings", "oz"),
                         reply_markup=keyboards.get_settings_menu(message.chat.id))


@dp.message_handler(text="Созламмалар")
async def send_settings(message: Message):
    await message.answer(text=get_string_by_language("settings", "uz"),
                         reply_markup=keyboards.get_settings_menu(message.chat.id))


@dp.message_handler(text="Настройки")
async def send_settings(message: Message):
    await message.answer(text=get_string_by_language("settings", "ru"),
                         reply_markup=keyboards.get_settings_menu(message.chat.id))


@dp.message_handler(text="Settings")
async def send_settings(message: Message):
    await message.answer(text=get_string_by_language("settings", "en"),
                         reply_markup=keyboards.get_settings_menu(message.chat.id))


# home button for different user languages
@dp.message_handler(text="Bosh bo'lim")
async def send_main_menu(message: Message):
    await message.answer(text=get_string_by_language("home", "oz"),
                         reply_markup=keyboards.get_main_menu(message.chat.id))


@dp.message_handler(text="Бош бўлим")
async def send_main_menu(message: Message):
    await message.answer(text=get_string_by_language("home", "uz"),
                         reply_markup=keyboards.get_main_menu(message.chat.id))


@dp.message_handler(text="Главное меню")
async def send_main_menu(message: Message):
    await message.answer(text=get_string_by_language("home", "ru"),
                         reply_markup=keyboards.get_main_menu(message.chat.id))


@dp.message_handler(text="Main menu")
async def send_main_menu(message: Message):
    await message.answer(text=get_string_by_language("home", "en"),
                         reply_markup=keyboards.get_main_menu(message.chat.id))


# about bot button result for user's different interface languages
@dp.message_handler(text="Bot haqida")
async def send_about(message: Message):
    await message.answer(text=get_string_by_language("about", "oz"),
                         reply_markup=keyboards.get_main_menu(message.chat.id))


@dp.message_handler(text="Бот ҳақида")
async def send_about(message: Message):
    await message.answer(text=get_string_by_language("about", "uz"),
                         reply_markup=keyboards.get_main_menu(message.chat.id))


@dp.message_handler(text="О боте")
async def send_about(message: Message):
    await message.answer(text=get_string_by_language("about", "ru"),
                         reply_markup=keyboards.get_main_menu(message.chat.id))


@dp.message_handler(text="About bot")
async def send_about(message: Message):
    await message.answer(text=get_string_by_language("about", "en"),
                         reply_markup=keyboards.get_main_menu(message.chat.id))


# button for changing language in different languages
@dp.message_handler(text="Tilni o'zgartirish")
async def change_language(message: Message):
    await message.answer(text=choose_language_action_text, reply_markup=keyboards.CHANGE_LANGUAGE_MENU)


@dp.message_handler(text="Тилни ўзгартириш")
async def change_language(message: Message):
    await message.answer(text=choose_language_action_text, reply_markup=keyboards.CHANGE_LANGUAGE_MENU)


@dp.message_handler(text="Сменить язык")
async def change_language(message: Message):
    await message.answer(text=choose_language_action_text, reply_markup=keyboards.CHANGE_LANGUAGE_MENU)


@dp.message_handler(text="Change language")
async def change_language(message: Message):
    await message.answer(text=choose_language_action_text, reply_markup=keyboards.CHANGE_LANGUAGE_MENU)


# change language action
async def inform_language_changed(message: Message):
    await message.bot.delete_message(message.chat.id, message.message_id)
    await message.answer(text=get_string("can_change_language", message.chat.id),
                         reply_markup=keyboards.get_main_menu(message.chat.id))
