from pydantic import Field
from typing import Optional

from .base import BaseSchema

class HHDemographicBase(BaseSchema):
    age_desc: Optional[str] = Field(None, max_length=20)
    marital_status_code: Optional[str] = Field(None, max_length=10)
    income_desc: Optional[str] = Field(None, max_length=50)
    homeowner_desc: Optional[str] = Field(None, max_length=20)
    hh_comp_desc: Optional[str] = Field(None, max_length=50)
    household_size_desc: Optional[str] = Field(None, max_length=10)
    kid_category_desc: Optional[str] = Field(None, max_length=30)
    household_key: int = Field(..., gt=0)

class HHDemographicCreate(HHDemographicBase):
    ...