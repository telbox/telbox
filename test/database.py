from telbox.database import  *
from datetime import  datetime
now = datetime.now

f = File(name ='', last_mtime=now(), parent_id = None, is_file = False, id = 1)
fn = File(name ='sb', last_mtime=now(), parent_id = 1, is_file = False)
session.add_all([f,fn])
session.commit()
import  ipdb; ipdb.set_trace()