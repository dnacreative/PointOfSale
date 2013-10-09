'''
One-time use script to set up database tables and perform other administrative tasks
'''
from pos import db

db.Base.metadata.create_all(db.engine)
