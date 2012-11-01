from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.types import Integer, String, Numeric
from sqlalchemy.schema import Column, ForeignKey

from pos import app_settings

#engine = create_engine('postgresql:///' + app_settings.db_name)
# using sqlite for testing (will switch to postgres later)
engine = create_engine('sqlite:///:memory:', echo=True)

session = scoped_session(sessionmaker(bind=engine, autoflush=False))
Base = declarative_base(bind=engine)

class Product(Base):
    __tablename__ = 'inventory_historical'

    id = Column(Integer, primary_key=True, nullable=False)
    vendor_id = Column(Integer, ForeignKey('vendors.id'), nullable=False)
    dept_id = Column(Integer, ForeignKey('departments.id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    quantity = Column(Integer, nullable=False)
    cost = Column(Numeric(19, 4), nullable=False)
    price = Column(Numeric(19, 4), nullable=False)

    # specify the one-to-one relationship between historical products and the list of current products
    current = relationship("CurrentProduct", uselist=False, backref="item")

    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

class CurrentProduct(Base):
    __tablename__ = 'inventory_current'

    id = Column(Integer, primary_key=True, nullable=False)
    historical_id = Column(Integer, ForeignKey('inventory_historical.id'), nullable=False)

class Vendor(Base):
    __tablename__ = 'vendors'

    id = Column(Integer, primary_key=True, nullable=False)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)

    product = relationship("Product")

    def __init__(self, code, name):
        self.code = code
        self.name = name

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, nullable=False)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)

    product = relationship("Product")

    def __init__(self, code, name):
        self.code = code
        self.name = name

class Adjustment(Base):
    __tablename__ = 'adjustments'

    id = Column(Integer, primary_key=True, nullable=False)
    item_id = Column(Integer, ForeignKey('inventory_historical.id'), nullable=False)
    old_cost = Column(Numeric(19, 4), nullable=False)
    old_price = Column(Numeric(19, 4), nullable=False)
    new_cost = Column(Numeric(19, 4), nullable=False)
    new_price = Column(Numeric(19, 4), nullable=False)

    item = relationship("Product", backref=backref('adjustments', order_by=id))
