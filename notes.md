# Considerations

quantity - numeric/decimal type to support e.g. selling food by weight  
may not be compatible with some systems that have stricter table creation requirements (see [sqlalchemy ORM tutorial](http://docs.sqlalchemy.org/en/rel_0_8/orm/tutorial.html) for an example)

# Misc
    
execute modules with -m (e.g., from project root, `python -m pos.tests.db_tests`) to allow imports to work properly

if flask debug is set, need to set PYTHONPATH=. before executing

examples of sqlalchemy testing
- http://stackoverflow.com/questions/833626/i-need-a-sample-of-python-unit-testing-sqlalchemy-model-with-nose
- http://sontek.net/blog/detail/writing-tests-for-pyramid-and-sqlalchemy

flask quickstart: http://flask.pocoo.org/docs/quickstart/#quickstart
