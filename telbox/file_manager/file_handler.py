from telbox.config import get_config
from pathlib import Path
from telbox.bot import Bot
from telbox.database import File,session
import logging
from telegram.message import Message
from .base import ScannerBase as Base
from datetime import datetime
config = get_config()
CHAT_ID = config.get("TELEGRAM_CHAT_ID")


class FileHandler(Base):
    def __init__(self, file: Path):
        self.file = file
        self.chat_id = CHAT_ID
        self.file_db = None

    @property
    def name(self):
        return self.file.name

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
        f = session.query(File).filter_by(name=self.name, is_file=self.is_file, parent= self.find_parent()).first()
        self.file_db = f
        return f

    def find_parent(self):
        parent = self.file.parent
        parent_id = 1
        parents = [parent]
        while True:
            if parent == self.get_home():
                break
            parent = parent.parent
            parents.append(parent)
        parent = session.query(File).get(parent_id)
        for parent_path in parents[::-1]:
            new_parent = session.query(File).filter_by(parent_id=parent.id, is_file=False,name=parent_path.name ).first()
            if not new_parent:
                new_parent = File(name=parent_path.name, parent_id=parent.id, is_file=False)
                session.add(new_parent)
                session.commit()
                print('='*8,new_parent)
            parent = new_parent
  
        return parent

    @property
    def modifcation_time(self):
        return  datetime.fromtimestamp(self.file.stat().st_mtime)

    def update_database(self, msg: Message):
        id = msg.message_id
        upload_time = msg.date
        chat_id = msg.chat.id
        document = msg.document.file_id
        file_size = msg.document.file_size
        unique_id = msg.document.file_unique_id
        last_mtime = self.modifcation_time
        # import ipdb; ipdb.set_trace()
        file = self.file
        exist = self.exist
        if exist:
            f = self.file_db
        else:
            f = File(name = file.name, parent = self.find_parent())
            session.add(f)
        f.upload_time = upload_time
        f.chat_id = chat_id
        f.document = document
        f.file_size = file_size
        f.unique_id = unique_id
        f.last_mtime = last_mtime
        session.commit()
        



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
        msg = Bot.send_document(
            self.chat_id,
            document=open(file),
            filename=file.name,
            caption=f"{str(file)};{self.modifcation_time}",
        )
        self.update_database(msg)
        logging.info(f"Uploading  {self.file} is finished")

    def update_file(self):
        if self.is_dir:
            return None

        if self.should_split:
            self.upload_split()
        else:
            self.upload_single()
