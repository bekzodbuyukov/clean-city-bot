# put your bot declarings here
import asyncio

from aiogram import Bot, Dispatcher, executor
from settings import config
from db import db_controller


# initializing database, if force=True, database will be recreated
db_controller.init_db()


# declaring the bot and its settings
loop = asyncio.get_event_loop()
bot = Bot(token=config.API_TOKEN, parse_mode='Markdown')
dp = Dispatcher(bot)

if __name__ == '__main__':
    # needed for answering to the user messages to bot
    from handlers.static_commands import dp
    
    executor.start_polling(dp, skip_updates=True)
