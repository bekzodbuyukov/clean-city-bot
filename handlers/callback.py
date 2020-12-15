from bot import dp
from aiogram.types import CallbackQuery
from handlers import static_commands
from db import db_controller


@dp.callback_query_handler()
async def callback_handler(call: CallbackQuery):
    # await call.message.answer()

    global language
    if call.data.startswith("oz_"):
        language = "oz"
    elif call.data.startswith("uz_"):
        language = "uz"
        text = "Тил созламмалари сакланди."
    elif call.data.startswith("ru_"):
        language = "ru"
        text = "Настройки языка сохранены"
    elif call.data.startswith("en_"):
        language = "en"
        text = "Language settings are saved."

    db_controller.add_data(user_id=call.message.chat.id, phone_number=0, language=language)
    await static_commands.set_user_phone_number(call.message)
