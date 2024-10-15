from pydantic import BaseModel, Field
from enum import Enum

class HealthLiveStatus(str, Enum):
    LIVE = "live"

class HealthLiveBase(BaseModel):
    state: HealthLiveStatus = Field(default=HealthLiveStatus.LIVE)

class HealthLivePublic(HealthLiveBase):
    pass
