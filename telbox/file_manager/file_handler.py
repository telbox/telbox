from telbox.config import get_config
from pathlib import Path
from telbox.bot import Bot
import logging
from telegram.message import Message

config = get_config()
CHAT_ID = config.get("TELEGRAM_CHAT_ID")


class FileHandler:
    def __init__(self, file: Path):
        self.file = file
        self.chat_id = CHAT_ID

    @property
    def is_file(self):
        return self.file.is_file()

    @property
    def is_dir(self):
        return self.file.is_dir()

    @property
    def size(self):
        return self.file.stat().st_size

    @property
    def should_split(self):
        return self.size > (50 * 1024 * 1023)

    @property
    def exist(self):
        # check database to see if file exist or not
        raise NotImplementedError
    @property 
    def modifcation_time(self):
        return self.file.stat().st_mtime
    def update_database(self, msg: Message):
        id = msg.message_id
        date = msg.date
        chat_id = msg.chat.id
        document = msg.document.file_id
        file_size = msg.document.file_size
        unique_id = msg.document.file_unique_id
        mtime = 
        # update database after each action
        raise NotImplementedError

    def upload_split(self):
        logging.info("Start Spliting")
        file = self.file

        with open(self.file, "rb") as f:
            counter = 0
            while True:
                counter += 1

                c = f.read(1024 * 1024 * 50)
                if not c:
                    break
                Bot.send_document(
                    self.chat_id,
                    document=open(file),
                    filename=file.name + f".part{counter}",
                )
        logging.info("End Spliting")

    def upload_single(self):
        file = self.file
        logging.info(f"Uploading file {self.file.name}")
        bx = Bot.send_document(self.chat_id, document=open(file), filename=file.name)
        import ipdb

        ipdb.set_trace()
        logging.info(f"Uploading  {self.file} is finished")

    def update_file(self):
        if self.is_dir:
            return None

        if self.should_split:
            self.upload_split()
        else:
            self.upload_single()
