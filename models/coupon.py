from sqlalchemy import Column, Integer, BigInteger, PrimaryKeyConstraint
from database import Base

class Coupon(Base):
    __tablename__ = 'coupon'
    __table_args__ = (
        PrimaryKeyConstraint('coupon_upc', 'campaign_id'),
        {'schema': 'raw'}
    )

    coupon_upc = Column(BigInteger, nullable=False, index=True)   # Штрихкод продукта (может быть пустым)
    product_id = Column(Integer, nullable=False, index=True)
    campaign_id = Column(Integer, nullable=False, index=True)

    def __repr__(self):
        return f"<Coupon(coupon_upc='{self.coupon_upc}', campaign_id={self.campaign_id})>"