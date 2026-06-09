from sqlalchemy import Column, Integer, String

from database import Base

class CampaignDesc(Base):
    __tablename__ = 'campaign_desc'
    __table_args__ = {'schema': 'raw'}

    description = Column(String(10), nullable=True)
    campaign = Column(Integer, primary_key=True, index=True)
    start_day = Column(Integer, nullable=True)
    end_day = Column(Integer, nullable=True)

    def __repr__(self):
        return f"<CampaignDesc(campaign={self.campaign}, description='{self.description}')>"