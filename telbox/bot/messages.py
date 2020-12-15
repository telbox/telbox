from telegram.ext import MessageHandler, Filters

from telegram.ext.callbackcontext import CallbackContext as Context
from telegram.update import Update


def echo(update: Update, context: Context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
