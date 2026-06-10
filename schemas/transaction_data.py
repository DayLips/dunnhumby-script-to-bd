from pydantic import Field
from typing import Optional

from .base import BaseSchema

class TransactionDataBase(BaseSchema):
    household_key: int = Field(..., gt=0)
    basket_id: int = Field(..., gt=0)
    day: int = Field(..., ge=0)
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., ge=0)
    sales_value: float = Field(..., ge=0)
    store_id: int = Field(..., gt=0)
    retail_disc: Optional[float] = Field(None)
    trans_time: Optional[int] = Field(None, ge=0)
    week_no: int = Field(..., ge=0)
    coupon_disc: Optional[float] = Field(None)
    coupon_match_disc: Optional[float] = Field(None)

class TransactionDataCreate(TransactionDataBase):
    ...