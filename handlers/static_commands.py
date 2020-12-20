from bot import dp, bot
from aiogram import types
from aiogram.types import Message, InputMedia
from keyboards import keyboards
from db import db_controller
from localizations.locals import get_string
from localizations import strings


@dp.message_handler(commands="start")
async def send_welcome(message: Message):
    """ Function for welcoming new and registered users """
    if db_controller.find_user(user_id=message.chat.id) != 0:
        await message.answer(text=get_string("welcome", message.chat.id).format(message.chat.first_name),
                             reply_markup=keyboards.get_main_menu(message.chat.id))
    else:
        await message.answer(text=strings.choose_language_action_text,
                             reply_markup=keyboards.CHOOSE_LANGUAGE_MENU)


async def set_user_phone_number(message: Message):
    """ Function for continuation of registration, after User chooses interface language"""
    text = get_string("lang_settings_saved", message.chat.id) \
           + "\n\n" + get_string("ask_phone_number", message.chat.id)

    # deleting previous sent message to keep chat with user clean
    await message.bot.delete_message(message.chat.id, message.message_id)

    await message.answer(text=text,
                         reply_markup=keyboards.get_share_number_menu(message.chat.id))


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: Message):
    """ Function for getting user's phone number to finish registration """
    # deleting previous sent message to keep chat with user clean
    await message.bot.delete_message(message.chat.id, message.message_id - 1)

    text = get_string("number_successfully_saved", message.chat.id)\
           + "\n\n" + get_string("can_change_language", message.chat.id)

    # deleting previous sent message to keep chat with user clean
    await message.bot.delete_message(message.chat.id, message.message_id)

    # working with database
    if db_controller.get_data(user_id=message.chat.id, needed_column="phone_number") == 0:
        try:
            db_controller.update_data(user_id=message.chat.id, updating_column="phone_number",
                                      updating_value=message.contact.phone_number)
        except:
            error_text = get_string("phone_number_error", message.chat.id)
            await message.answer(text=error_text)
        await message.answer(text=text, reply_markup=keyboards.get_main_menu(message.chat.id))
    else:
        await message.answer(text=get_string("number_not_needed", message.chat.id),
                             reply_markup=keyboards.get_main_menu(message.chat.id))


# @dp.message_handler(content_types=types.ContentTypes.PHOTO)
# async def get_problem_photos(message: Message):
#     problem_photos = message.photo
#     if message.photo:
#         print("Photo is received!")
#     # await message.answer_photo(photo="https://image.freepik.com/free-vector/illustration-human-avatar-with-environment_53876-17627.jpg")
#     await message.answer_media_group(media="https://image.freepik.com/free-vector/illustration-human-avatar-with-environment_53876-17627.jpg",
#                                             "https://image.freepik.com/free-vector/garbage-waste-recycling-isometric-composition-with-conceptual-images-colourful-bins-different-groups-rubbish-vector-illustration_1284-30708.jpg"])
