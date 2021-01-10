from .base import  Base, engine, session
from .models import  File

Base.metadata.create_all(engine)