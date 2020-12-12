from bot import dp
from aiogram.types import Message
from keyboards import keyboards
from db.db_controller import db, User, db_query

# creating the global instance of the class User
User = User()


@dp.message_handler(commands="start")
async def send_welcome(message: Message):
    if db.search(db_query.id == message.chat.id):
        await message.answer(f"Assalomu alaykum, {message.chat.full_name}!", reply_markup=keyboards.MAIN_MENU)
    else:
        User.set_id(message.chat.id)
        choose_language_action_text = f"Iltimos, tilni tanlang.\n\n" \
                                      f"Пожалуйста, выберите язык.\n\n" \
                                      f"Please, choose the language."
        await message.answer(text=choose_language_action_text, reply_markup=keyboards.CHOOSE_LANGUAGE_MENU)

        print(User.id)


async def register_user_language(user_language):
    User.set_language(user_language)
    print(user_language)


async def set_user_phone_number(message: Message):
    await message.answer(text="test", reply_markup=keyboards.MAIN_MENU)
