from sqlalchemy import Column, Integer, String, Enum
import enum

from database import Base

class ProductBrand(enum.Enum):
    National = 'National'
    Private = 'Private'

class Product(Base):
    __tablename__ = 'products'
    __table_args__ = {'schema': 'raw'}

    product_id = Column(Integer, primary_key=True, index=True)
    manufacturer = Column(Integer, index=True)
    department = Column(String(15), nullable=True, index=True)
    brand = Column(Enum(ProductBrand), nullable=True, index=True)
    commodity_desc = Column(String(30), nullable=True)
    sub_commodity_desc = Column(String(30), nullable=True)
    curr_size_of_product = Column(String(10), nullable=True)

    def __repr__(self):
        return f"<Product(id={self.id}, department='{self.department}', brand='{self.brand}')>"