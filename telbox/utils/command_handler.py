from telegram.ext import CommandHandler


def command(command_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return CommandHandler(command_name, func)

        return wrapper()

    return decorator
