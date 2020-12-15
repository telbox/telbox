from .base import dispatcher
from .commands import caps, start, upload
from .messages import echo_handler

## commands
dispatcher.add_handler(start)
dispatcher.add_handler(caps)
dispatcher.add_handler(upload)

## messages

dispatcher.add_handler(echo_handler)
