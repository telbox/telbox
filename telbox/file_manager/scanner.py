from .base import ScannerBase
from telbox.bot import Bot
import os


class Scanner(ScannerBase):
    def check_files(self):
        file_lists = os.listdir(self.home)
        for file in file_lists:
            self.update_file(file)

    def update_file(self, file):
        file = self.home / file
        file_size = file.stat().st_size
        print(file, file_size)
        limit = 50 * 1024 * 1024
        if file_size < limit:
            Bot.send_document(self.chat_id, document=open(file))


scanner = Scanner()
scanner.check_files()