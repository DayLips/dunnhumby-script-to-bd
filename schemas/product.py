from pydantic import Field
from typing import Optional

from .base import BaseSchema

class ProductBase(BaseSchema):
    product_id: int = Field(..., gt=0)
    manufacturer: Optional[int] = Field(None, gt=0)
    department: Optional[str] = Field(None, max_length=15)
    brand: Optional[str] = Field(None, max_length=10)
    commodity_desc: Optional[str] = Field(None, max_length=30)
    sub_commodity_desc: Optional[str] = Field(None, max_length=30)
    curr_size_of_product: Optional[str] = Field(None, max_length=10)

class ProductCreate(ProductBase):
    ...