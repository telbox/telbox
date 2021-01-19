from .base import ScannerBase
from telbox.bot import Bot
import os
from .file_handler import FileHandler
import glob

class Scanner(ScannerBase):
    def check_files(self):
        path = str(self.get_home())
        file_lists = glob.iglob(path+'/**/*', recursive=True)

        for file in file_lists:
            self.update_file(file)

    def update_file(self, file):
        file = self.home / file
        f = FileHandler(file)
        f.update_file()


scanner = Scanner()
scanner.check_files()

