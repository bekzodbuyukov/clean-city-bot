# put your bot declarings here
import asyncio

from aiogram import Bot, Dispatcher, executor
from settings import config


# declaring the bot
loop = asyncio.get_event_loop()
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    # needed for answering to the user messages to bot
    from handlers.static_commands import dp
    executor.start_polling(dp, skip_updates=True)
