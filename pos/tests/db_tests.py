'''
Database tests
'''
import unittest

from sqlalchemy import create_engine

from pos.db import db_session, Base, Vendor, Department, Item
from pos.app_settings import db_engine, db_test_name

# creating objects that instantiate the tables queries the DB
# therefore, only create them as needed rather than immediately on import
# (this is especially important with Items, which fetch Vendor/Dept IDs)
def get_test_vendors():
    return [
        Vendor('DGS', 'Douglas'),
        Vendor('PUT', 'Putamayo'),
        Vendor('ING', 'Ingram')
    ]
    
def get_test_depts():
    return [
        Department('PL', 'plush'),
        Department('MUS', 'music'),
        Department('FIC', 'fiction')
    ]
    
def get_test_items():
    return [
        Item('Snowy Owl', 'Douglas', 5, True, 5.00, 9.99, vendor_code='DGS', dept_code='PL'),
        Item('Celtic Tides', 'CD', 3, True, 10.00, 19.99, vendor_code='PUT', dept_code='MUS'),
        Item('Hunger Games', 'Collins/Ingram', 2, True, 4.00, 7.99, vendor_code='ING', dept_code='FIC')
    ]

class test_item_table(unittest.TestCase):
    def setUp(self):
        engine = create_engine(db_engine + '://' + db_test_name, echo = True, convert_unicode=True)
        db_session.configure(bind=engine)
        
    def test_add_item(self):
        pass
    
    def test_update_cost(self):
        pass
    
    def test_update_price(self):
        pass
        
    def tearDown(self):
        db_session.rollback()
    
def add_test_data():
    test_vendors = get_test_vendors()
    test_depts = get_test_depts()
    db_session.add_all(test_vendors + test_depts)
    
    db_session.commit()

    # add the items separately after the vendors/departments so the IDs will be set correctly
    test_items = get_test_items()
    db_session.add_all(test_items)
    
    db_session.commit()

if __name__ == '__main__':
    unittest.main()
