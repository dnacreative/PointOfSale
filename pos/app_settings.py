DEBUG = True

# flask stuff
secret_key = 'not implemented'

# sqlalchemy stuff
db_engine = 'sqlite'            # TODO: set up postgresql
db_name = '/pos/test.db'        # file used for sqlite; change to actual DB for postgres
db_test_name = '/pos/test.db'   # DB used for testing, preferably differs from production
# length of descriptive VARCHAR columns (item name, etc.)
long_length = 100
# length for abbreviated VARCHAR columns (codes, etc.)
short_length = 8
