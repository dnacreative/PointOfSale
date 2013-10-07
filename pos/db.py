import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.types import Integer, String, Numeric, Boolean, DateTime
from sqlalchemy.schema import Column, ForeignKey

from pos import app_settings

#engine = create_engine('postgresql:///' + app_settings.db_name)
# using sqlite for testing (will switch to postgres later)
engine = create_engine('sqlite:///:memory:', echo=True)

session = scoped_session(sessionmaker(bind=engine, autoflush=False))
Base = declarative_base(bind=engine)

class Item(Base):
    __tablename__ = 'items'

    item_id = Column(Integer, primary_key=True, nullable=False)
    vendor_id = Column(Integer, ForeignKey('vendors.id'))
    dept_id = Column(Integer, ForeignKey('departments.id'))
    # note: sqlalchemy String corresponds to SQL VARCHAR
    name = Column(String(app_settings.long_length), nullable=False)
    description = Column(String(app_settings.long_length))
    quantity = Column(Integer, nullable=False)
    tax = Column(Boolean, nullable=False)
    cost = Column(Numeric(19, 4), nullable=False)
    price = Column(Numeric(19, 4), nullable=False)

    def __init__(self, vendor_id, dept_id, name, description, quantity, tax, cost, price):
        self.vendor_id = vendor_id
        self.dept_id = dept_id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.tax = tax
        self.cost = cost
        self.price = price

class Vendor(Base):
    __tablename__ = 'vendors'

    vendor_id = Column(Integer, primary_key=True, nullable=False)
    vendor_code = Column(String(app_settings.short_length), nullable=False)
    vendor_name = Column(String(app_settings.long_length), nullable=False)

    #item = relationship("Item")

    def __init__(self, code, name):
        self.vendor_code = code
        self.vendor_name = name

class Department(Base):
    __tablename__ = 'departments'

    dept_id = Column(Integer, primary_key=True, nullable=False)
    dept_code = Column(String(app_settings.short_length), nullable=False)
    dept_name = Column(String(app_settings.long_length), nullable=False)

    #item = relationship("Item")

    def __init__(self, code, name):
        self.dept_code = code
        self.dept_name = name

class UPC(Base):
    __tablename__ = 'upcs'
    
    upc = Column(String(13), primary_key=True, nullable=False)
    item_id = Column(Integer, nullable=False)
    
    def __init__(self, upc, item_id):
        self.upc = upc
        self.item_id = item_id
        
class Adjustment(Base):
    __tablename__ = 'adjustments'

    adjustment_id = Column(Integer, primary_key=True, nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    adjustment_date = Column(DateTime, default=datetime.datetime.utcnow(), nullable=False)
    valid_date = Column(DateTime, default=datetime.datetime.utcnow(), nullable=False)
    adjustment_type = Column(String(app_settings.short_length), nullable=False)
    old_value = Column(Numeric(19, 4))
    new_value = Column(Numeric(19, 4))
    old_text = Column(String(app_settings.long_length))
    new_text = Column(String(app_settings.long_length))

    #item = relationship("Item", backref=backref('adjustments', order_by=id))
    
    def __init__(self, adj_id, item_id, adj_date, valid_date, adj_type, old_value, new_value, old_text, new_text):
        self.adjustment_id = adj_id
        self.item_id = item_id
        self.adjustment_date = adj_date
        self.valid_date = valid_date
        self.adjustment_type = adj_type
        self.old_value = old_value
        self.new_value = new_value
        self.old_text = old_text
        self.new_text = new_text
