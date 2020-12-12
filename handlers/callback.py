from bot import dp
from aiogram.types import CallbackQuery
from .static_commands import User, set_user_phone_number


@dp.callback_query_handler()
async def callback_handler(call: CallbackQuery):
    print("callback handler started its work")
    if call.data.startswith("oz_"):
        await User.set_language("oz")
        print("user's lang was set")
        await call.message.answer(text="Til sozlammalari saqlandi.\n\nIltimos telefon raqamingizni bo'lishing.")
        print("text was sent")
        await set_user_phone_number(call.message)
        print("done")
    elif call.data.startswith("uz_"):
        await call.message.answer(text="Тил созламмалари сакланди.")
    elif call.data.startswith("ru_"):
        await call.message.answer(text="Настройки языка сохранены")
    elif call.data.startswith("en_"):
        await call.message.answer(text="Language settings are saved.")
