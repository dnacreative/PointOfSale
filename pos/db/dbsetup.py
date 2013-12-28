'''
One-time use script to set up database tables and perform other administrative tasks
'''
import pos.db
from pos.db import Base, engine

def init_db():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    init_db()