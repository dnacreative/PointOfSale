'''
Unit tests for the database
'''
import unittest

from sqlalchemy import create_engine

from pos.db import session, Base, Item, Vendor, Department, UPC, Adjustment

class test_item_table(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_add_item(self):
        pass
    
    def test_update_cost(self):
        pass
    
    def test_update_price(self):
        pass
        
    def tearDown(self):
        pass
    
if __name__ == '__main__':
    unittest.main()
