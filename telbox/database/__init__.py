from .base import  Base, engine, session
from .models import  File
from datetime import datetime
Base.metadata.create_all(engine)

def init_db():
    if session.query(File).filter_by(id=1).first():
        return None
    else:
        print('create home at db')
        f = File(name='', is_file=False )
        session.add(f)
        session.commit()
init_db()
