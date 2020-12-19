from telbox.config import get_config
from pathlib import Path

config = get_config()
HOME = config.get("HOME")
CHAT_ID = config.get("TELEGRAM_CHAT_ID")


class ScannerBase:
    def __init__(self):
        self.home = self.get_home()
        self.chat_id = CHAT_ID

    def get_home(self):
        if HOME:
            home = Path(home)
        else:
            home = Path.home() / "telbox"

        home.mkdir(exist_ok=True)
        return home
