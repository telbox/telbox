import logging

import telegram
from telbox.config import get_config
from telegram.ext import Updater

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

config = get_config()

TOKEN = config.get("TELEGRAM_BOT_API")
Bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


if __name__ == "__main__":
    print(Bot.get_me())
