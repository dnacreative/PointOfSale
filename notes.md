# Considerations

quantity - numeric/decimal type to support e.g. selling food by weight  
may not be compatible with some systems that have stricter table creation requirements (see sqlalchemy ORM tutorial for an example: http://docs.sqlalchemy.org/en/rel_0_8/orm/tutorial.html)

# Misc
    
execute modules with -m (e.g., from project root, `python -m pos.tests.db_tests`) to allow imports to work properly
