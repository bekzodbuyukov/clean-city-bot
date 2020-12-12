import logging

from environs import Env


# reading .env file
env = Env()
env.read_env()

# turning on or off logging to file depending on boolean value from .env variable
LOGGING_ENABLED = env.bool("LOGGING_ENABLED")

if LOGGING_ENABLED:
    logging.basicConfig(filename="bot.log", level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

# checking if api token is available
API_TOKEN = env.str("API_TOKEN")

if not API_TOKEN:
    logging.error("Telegram BOT API Token is not found!")
