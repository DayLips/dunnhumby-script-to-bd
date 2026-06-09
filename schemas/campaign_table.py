from pydantic import Field
from typing import Optional

from .base import BaseSchema

class CampaignTableBase(BaseSchema):
    description: Optional[str] = Field(None, max_length=5)
    household_key: int = Field(..., gt=0)
    campaign_id: int = Field(..., gt=0)

class CampaignTableCreate(CampaignTableBase):
    ...