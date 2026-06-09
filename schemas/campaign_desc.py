from pydantic import Field
from typing import Optional

from .base import BaseSchema

class CampaignDescBase(BaseSchema):
    description: Optional[str] = Field(None, max_length=10)
    campaign: int = Field(..., gt=0)
    start_day: Optional[int] = Field(None, ge=0)
    end_day: Optional[int] = Field(None, ge=0)

class CampaignDescCreate(CampaignDescBase):
    ...