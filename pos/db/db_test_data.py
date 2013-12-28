'''
Add a few entries to the database for testing
'''
import pos.db
from pos.db import db_session, Vendor, Department, Item

test_vendors = [
    Vendor('DGS', 'Douglas'),
    Vendor('PUT', 'Putamayo'),
    Vendor('ING', 'Ingram')
]
test_depts = [
    Department('PL', 'plush'),
    Department('MUS', 'music'),
    Department('FIC', 'fiction')
]
test_items = [
    Item('Snowy Owl', 'Douglas', 5, True, 5.00, 9.99, vendor_code='DGS', dept_code='PL'),
    Item('Celtic Tides', 'CD', 3, True, 10.00, 19.99, vendor_code='PUT', dept_code='MUS'),
    Item('Hunger Games', 'Collins/Ingram', 2, True, 4.00, 7.99, vendor_code='ING', dept_code='FIC')
]

def add_test_data():
    # add objects to db
    pass
