import os
import shutil

from aiogram.dispatcher import FSMContext

from bot import bot, dp
from aiogram.types import Message, InputFile
from aiogram import types
from settings import config
from localizations.locals import get_string, get_string_by_language
from keyboards import keyboards
from aiogram.dispatcher.filters.state import State, StatesGroup


class Report(StatesGroup):
    image = State()
    caption = State()
    anonymous_mode = State()


# @dp.message_handler(state=Report.image)
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def get_problem_photos(message: Message, state: FSMContext):
    filename = "file_" + str(message.photo[-1].file_unique_id) + ".png"

    # await message.photo[-1].download(destination=storage_destination + filename)
    file = await bot.get_file(message.photo[-1].file_id)
    file_path = file.file_path

    await bot.download_file(file_path=file_path, destination=filename)

    downloaded_file = config.TEMP_MEDIA_DESTINATION + filename
    moved_file = config.FINAL_MEDIA_DESTINATION + filename

    if not os.path.exists(config.FINAL_MEDIA_DESTINATION + filename):
        shutil.move(downloaded_file, config.FINAL_MEDIA_DESTINATION)
    else:
        pass
        # os.remove(path=config.TEMP_MEDIA_DESTINATION + filename)

    await message.answer(text=get_string("ask_for_definition", message.chat.id),
                         reply_markup=keyboards.get_main_menu(message.chat.id))

    await state.update_data(image=moved_file)

    await Report.caption.set()
    print(downloaded_file, moved_file)
    print("Got image!")

    # await ask_for_problem_definition(message)

    # await bot.send_media_group(chat_id=message.chat.id, media=[InputMediaPhoto(media=first_image),
    #                                                            InputMediaPhoto(media=second_image),
    #                                                            InputMediaPhoto(media=third_image)])


@dp.message_handler(state=Report.caption)
async def ask_for_problem_definition(message: Message, state: FSMContext):
    await state.update_data(caption=message.text)

    await Report.anonymous_mode.set()
    print("Got definition!")
    await message.answer(text=get_string("want_to_be_anonymous", message.chat.id),
                         reply_markup=keyboards.get_stay_anonymous_menu(message.chat.id))


@dp.message_handler(lambda message: message.text == get_string("no_button", message.chat.id),
                    state=Report.anonymous_mode)
async def ask_if_anonymous(message: Message, state: FSMContext):
    async with state.proxy() as data:
        photo = data['image']
        caption = data['caption']
        print(data, caption)
        await bot.send_photo(chat_id=config.PROBLEMS_CHANNEL,
                             caption=get_string_by_language("problem_caption", "oz").format(caption,
                                                                                            message.chat.first_name,
                                                                                            message.chat.id),
                             photo=InputFile(path_or_bytesio=photo))

    await message.answer(text=get_string("thanks_for_report", message.chat.id),
                         reply_markup=keyboards.get_main_menu(message.chat.id))

    await state.finish()


@dp.message_handler(lambda message: message.text == get_string("yes_button", message.chat.id),
                    state=Report.anonymous_mode)
async def ask_if_anonymous(message: Message, state: FSMContext):
    async with state.proxy() as data:
        photo = data['image']
        caption = data['caption']
        print(data, caption)
        await bot.send_photo(chat_id=config.PROBLEMS_CHANNEL,
                             caption=get_string_by_language("problem_caption", "oz").format(caption,
                                                                                            "-",
                                                                                            config.PROBLEMS_CHANNEL),
                             photo=InputFile(path_or_bytesio=photo))

    await message.answer(text=get_string("thanks_for_report", message.chat.id),
                         reply_markup=keyboards.get_main_menu(message.chat.id))

    await state.finish()
