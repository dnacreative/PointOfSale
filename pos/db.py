from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.types import Integer, String
from sqlalchemy.schema import Column, ForeignKey

from pos import app_settings

engine = create_engine('postgresql:///' + app_settings.db_name)
session = scoped_session(sessionmaker(bind=engine, autoflush=False))
Base = declarative_base(bind=engine)

class Product(Base):
    __tablename__ = 'inventory_historical'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    # TODO: columns for department and vendor (linked to other tables with more info), cost and price,
    #       quantity, link to cost/price adjustment table, keywords

    # specify the one-to-one relationship between historical products and the list of current products
    current = relationship("CurrentProduct", uselist=False, backref="inventory_historical")

class CurrentProduct(Base):
    __tablename__ = 'inventory_current'

    id = Column(Integer, primary_key=True, nullable=False)
    historical_id = Column(Integer, ForeignKey('inventory_historical.id'), nullable=False)

