import logging

from telegram.ext import Filters, MessageHandler
from telegram.ext.callbackcontext import CallbackContext as Context
from telegram.update import Update


def echo(update: Update, context: Context):
    logging.info(f"chat_id: {update.effective_chat.id}")

    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
