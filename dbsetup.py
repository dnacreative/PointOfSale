import app_settings

from sqlalchemy import create_engine

try:
    engine = create_engine('postgresql:///' + app_settings.db_name, echo=True)
except:
    # couldn't connect to db probably means it doesn't exist or bad permissions