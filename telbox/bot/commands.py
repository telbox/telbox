from pathlib import Path

from telbox.utils import command
from telegram.ext import CommandHandler, Handler
from telegram.ext.callbackcontext import CallbackContext as Context
from telegram.update import Update


@command("start")
def start(update: Update, context: Context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


@command("caps")
def caps(update: Update, context: Context):
    text_caps = " ".join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


@command("upload")
def upload(update: Update, context: Context):
    readme = Path("/home/mehdi/Documents/Projects/telbox/telbox/README.md")
    context.bot.send_document(chat_id=update.effective_chat.id, document=open(readme))
