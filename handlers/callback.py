from bot import dp
from aiogram.types import CallbackQuery
from handlers import static_commands
from db.db_controller import UserModel


@dp.callback_query_handler()
async def callback_handler(call: CallbackQuery):
    user = UserModel()
    user.set_id(call.message.chat.id)
    if call.data.startswith("oz_lang"):
        user.set_language("oz")
        # await call.message.answer()
        await static_commands.set_user_phone_number(call.message, user)
    elif call.data.startswith("uz_"):
        user.set_language("uz")
        await call.message.answer(text="Тил созламмалари сакланди.")
    elif call.data.startswith("ru_"):
        user.set_language("ru")
        await call.message.answer(text="Настройки языка сохранены")
    elif call.data.startswith("en_"):
        user.set_language("en")
        await call.message.answer(text="Language settings are saved.")
