from sqlalchemy import Column, Integer, String

from database import Base

class HHDemographic(Base):
    __tablename__ = 'hh_demographic'
    __table_args__ = {'schema': 'raw'}

    id = Column(Integer, primary_key=True, index=True)
    age_desc = Column(String(20), nullable=True)
    marital_status_code = Column(String(10), nullable=True)
    income_desc = Column(String(50), nullable=True)
    homeowner_desc = Column(String(20), nullable=True)
    hh_comp_desc = Column(String(50), nullable=True)
    household_size_desc = Column(String(10), nullable=True)
    kid_category_desc = Column(String(30), nullable=True)
    household_key = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f"<HHDemographic(household_key={self.household_key}, age_desc='{self.age_desc}')>"