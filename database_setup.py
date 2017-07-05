import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Product(Base):
	__tablename__ = 'product'

	id =   Column(Integer, primary_key=True)
	product_id = Column(String, primary_key=True, autoincrement=False)
	product_name = Column(String(250), nullable=False)
	product_price = Column(Integer, nullable=False)
	product_description = Column(Integer, nullable=False)
	product_price = Column(Integer, nullable=False)
"""class MenuItem(Base):
	__tablename__ = 'menu_item'

	name = Column(String(250), nullable=False)
	id =   Column(Integer, primary_key=True)
	description = Column(String(250))
	price = Column(String(8))
	course = Column(String(250))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)"""

#at end of file
#engine = create_engine('sqlite:///restaurantmenu.db')
engine = create_engine('mysql+pymysql://root:toor@127.0.0.1:3306')
engine.execute("CREATE DATABASE resmenu")
Base.metadata.create_all(engine)








 