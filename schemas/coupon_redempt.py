from pydantic import Field

from .base import BaseSchema

class CouponRedemptBase(BaseSchema):
    household_key: int = Field(..., gt=0)
    day: int = Field(..., ge=0)
    coupon_upc: int = Field(..., gt=0)
    campaign_id: int = Field(..., gt=0)

class CouponRedemptCreate(CouponRedemptBase):
    ...