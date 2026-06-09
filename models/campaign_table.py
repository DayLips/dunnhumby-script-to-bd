from sqlalchemy import Column, Integer, BigInteger, String, PrimaryKeyConstraint

from database import Base

class CampaignTable(Base):
    __tablename__ = 'campaign_table'
    __table_args__ = (
        PrimaryKeyConstraint('household_key', 'campaign_id'),
        {'schema': 'raw'}
     )

    description = Column(String(5), nullable=True)                  # Описание кампании
    household_key = Column(BigInteger, nullable=False, index=True)  # Индекс для поиска по домохозяйствам
    campaign_id = Column(Integer, nullable=False, index=True)       # Индекс для группировки по кампаниям

    def __repr__(self):
        return f"<CampaignTable(household_key={self.household_key}, campaign_id={self.campaign_id})>"