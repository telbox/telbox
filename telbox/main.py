from telbox.bot import updater, Bot
from telbox.config import get_config

get_config()
print(Bot.get_me())
updater.start_polling()
