from pydantic import Field

from .base import BaseSchema

class CouponBase(BaseSchema):
    coupon_upc: int = Field(..., gt=0)
    product_id: int = Field(..., gt=0)
    campaign_id: int = Field(..., gt=0)

class CouponCreate(CouponBase):
    ...