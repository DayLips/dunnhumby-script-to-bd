from sqlalchemy import Column, Integer, BigInteger
from database import Base

class CouponRedempt(Base):
    __tablename__ = 'coupon_redempt'
    __table_args__ = {'schema': 'raw'}

    id = Column(Integer, primary_key=True, index=True)
    household_key = Column(BigInteger, nullable=False, index=True)
    day = Column(Integer, nullable=False, index=True)          
    coupon_upc = Column(BigInteger, nullable=False, index=True)
    campaign_id = Column(Integer, nullable=False, index=True)  

    def __repr__(self):
        return f"<CouponRedempt(household_key={self.household_key}, coupon_upc={self.coupon_upc}, day={self.day})>"