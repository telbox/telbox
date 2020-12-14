import telegram
from telbox.config import get_config

config = get_config()

TOKEN = config.get("TELEGRAM_BOT_API")
Bot = telegram.Bot(token=TOKEN)
