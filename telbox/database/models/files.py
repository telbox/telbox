from .. import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import backref, relationship
from pathlib import Path
from datetime import datetime
from telbox.config import get_config

config = get_config()
HOME = config.get("HOME")


class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    last_mtime = Column(DateTime, nullable=False, default =datetime.now )
    upload_time = Column(DateTime, nullable=True)
    is_file = Column(Boolean, default=True)
    document = Column(String)
    file_size = Column(Integer)
    unique_id = Column(String)
    chat_id = Column(Integer)



    @property
    def path(self):
        if self.id == 1:
            if HOME:
               home = Path(HOME)
            else:
                home = Path.home() / "telbox"
            return Path(home)
        return self.parent.path / self.name
    def __repr__(self):
        return f'path: {self.path}; file: {self.is_file}'

File.parent_id = Column(Integer, ForeignKey("files.id"), nullable=True,default=1)
File.parent = relationship(File,remote_side=File.id,backref='children')