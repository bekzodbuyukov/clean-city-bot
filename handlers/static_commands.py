import shutil, os

from bot import dp, bot
from aiogram import types
from aiogram.types import Message, InputMedia, InputMediaPhoto, input_media, InputFile
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


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def get_problem_photos(message: Message):
    first_image = "https://image.freepik.com/free-vector/illustration-human-avatar-with-environment_53876-17627.jpg"
    second_image = "https://image.freepik.com/free-vector/garbage-waste-recycling-isometric-composition-with-"\
                   + "conceptual-images-colourful-bins-different-groups-rubbish-vector-illustration_1284-30708.jpg"
    third_image = "https://image.freepik.com/free-vector/green-energy-urban-landscape-vector-ecology-nature-eco"\
                  + "-house-building-green-energy-eco-city-vector-landscape-illustration_1284-46239.jpg"

    temp_destination = "/home/bek/myFiles/clean-city-bot/"
    final_destination = "/home/bek/myFiles/clean-city-bot/user_media/photos/"
    filename = "file_" + str(message.photo[-1].file_unique_id) + ".png"

    # await message.photo[-1].download(destination=storage_destination + filename)
    file = await bot.get_file(message.photo[-1].file_id)
    file_path = file.file_path
    # print(file_path)
    await bot.download_file(file_path=file_path, destination=filename)

    downloaded_file = temp_destination + filename

    if not os.path.exists(final_destination + filename):
        shutil.move(downloaded_file, final_destination)

    problem_caption = f"Yangi muammo!\n\nBot: [@toza_shahar_bot](@toza_shahar_bot)\n"\
                      f"Muammo muallifi: [{str(message.chat.first_name)}]"\
                      f"(tg://user?id={str(message.chat.id)})"

    await bot.send_photo(chat_id=-1001184010608, caption=problem_caption,
                         photo=InputFile(path_or_bytesio=final_destination + filename))

    await message.answer(text=get_string("thanks_for_report", message.chat.id),
                         reply_markup=keyboards.get_main_menu(message.chat.id))

    # await bot.send_media_group(chat_id=message.chat.id, media=[InputMediaPhoto(media=first_image),
    #                                                            InputMediaPhoto(media=second_image),
    #                                                            InputMediaPhoto(media=third_image)])
