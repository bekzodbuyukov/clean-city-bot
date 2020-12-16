from bot import dp
from aiogram.types import CallbackQuery
from handlers import static_commands, user_commands
from db import db_controller


@dp.callback_query_handler()
async def handle_set_language_callback(call: CallbackQuery):
    """ Function for handling CallBack data """
    # await call.message.answer()

    global language
    if call.data.startswith("oz_"):
        language = "oz"
        db_controller.add_data(user_id=call.message.chat.id,
                               phone_number=0,
                               language=language)
        await static_commands.set_user_phone_number(call.message)
    elif call.data.startswith("uz_"):
        language = "uz"
        db_controller.add_data(user_id=call.message.chat.id,
                               phone_number=0,
                               language=language)
        await static_commands.set_user_phone_number(call.message)
    elif call.data.startswith("ru_"):
        language = "ru"
        db_controller.add_data(user_id=call.message.chat.id,
                               phone_number=0,
                               language=language)
        await static_commands.set_user_phone_number(call.message)
    elif call.data.startswith("en_"):
        language = "en"
        db_controller.add_data(user_id=call.message.chat.id,
                               phone_number=0,
                               language=language)
        await static_commands.set_user_phone_number(call.message)
    elif call.data.startswith("to_oz_"):
        language = "oz"
        db_controller.update_data(user_id=call.message.chat.id,
                                  updating_column="language",
                                  updating_value=language)
        await user_commands.inform_language_changed(call.message)
    elif call.data.startswith("to_uz_"):
        language = "uz"
        db_controller.update_data(user_id=call.message.chat.id,
                                  updating_column="language",
                                  updating_value=language)
        await user_commands.inform_language_changed(call.message)
    elif call.data.startswith("to_ru_"):
        language = "ru"
        db_controller.update_data(user_id=call.message.chat.id,
                                  updating_column="language",
                                  updating_value=language)
        await user_commands.inform_language_changed(call.message)
    elif call.data.startswith("to_en_"):
        language = "en"
        db_controller.update_data(user_id=call.message.chat.id,
                                  updating_column="language",
                                  updating_value=language)
        await user_commands.inform_language_changed(call.message)
