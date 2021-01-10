from .. import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import backref, relationship
from pathlib import Path
from telbox.config import get_config

config = get_config()
HOME = config.get("HOME")


class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    last_mtime = Column(DateTime, nullable=False)
    upload_time = Column(DateTime, nullable=True)
    is_file = Column(Boolean, default=True)

    parent_id = Column(Integer, ForeignKey('files.id'), nullable=True, default=1)
    parent = relationship("File", backref='child')

    @property
    def path(self):
        if self.id == 1:
            if HOME:
               home = Path(HOME)
            else:
                home = Path.home() / "telbox"
            return Path(home)
        return self.parent.path / self.name