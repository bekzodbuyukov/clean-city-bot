from bot import dp
from aiogram import types
from aiogram.types import Message
from keyboards import keyboards
from db import db_controller


@dp.message_handler(commands="start")
async def send_welcome(message: Message):
    """ Function for welcoming new and registered users """
    # if db.search(db_query.id == message.chat.id):
    if db_controller.find_user(user_id=message.chat.id) != 0:
        welcome_oz_text = f"Assalomu alaykum, [foydalanuvchi](tg://user?id={message.chat.id})!"
        await message.answer(text=welcome_oz_text,
                             reply_markup=keyboards.MAIN_MENU)
    else:
        choose_language_action_text = f"Iltimos, tilni tanlang.\n\n" \
                                      f"Пожалуйста, выберите язык.\n\n" \
                                      f"Please, choose the language."
        await message.answer(text=choose_language_action_text,
                             reply_markup=keyboards.CHOOSE_LANGUAGE_MENU)


async def set_user_phone_number(message: Message):
    """ Function for continuation of registration, after User chooses interface language"""
    share_contact_oz_text = "Til sozlammalari saqlandi.\n\nIltimos telefon raqamingizni bo'lishing."

    # print(f"{user.id} - {user.language} - {user.phone_number}")

    # try:
    #     db.insert({'id': user.id, 'language': user.language, 'phone_number': 0, 'status': 'True'})
    # except:
    #     pass

    await message.answer(text=share_contact_oz_text,
                         reply_markup=keyboards.SHARE_CONTACT_MENU)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: Message):
    successfully_registered_text = "Telefon raqamingiz muvaffaqiyatli ravishda saqlandi.\n\n" \
                                   "Til sozlammalarini istalgan vaqt:\n *Sozlamallar* -> *Tilni o'zgartirish* " \
                                   "\nbo'limidan o'zgartirishingiz mumkin."
    # print(f"{message.contact.phone_number}")

    # working with database
    try:
        db_controller.update_data(user_id=message.chat.id, updating_column="phone_number",
                                  updating_value=message.contact.phone_number)
        # db.update({'phone_number': message.contact.phone_number}, db_query.id == message.chat.id)
    except:
        sorry_text_oz = "Uzr, xatolik yuz berdi. Iltimos, /start buyrug'ini jo'natgan holda boshqatdan urunib ko'ring."
        await message.answer(text=sorry_text_oz)

    await message.answer(text=successfully_registered_text, reply_markup=keyboards.MAIN_MENU)