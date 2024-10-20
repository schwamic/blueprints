from enum import Enum

from pydantic import BaseModel, Field


class HealthLiveStatus(str, Enum):
    LIVE = "live"


class HealthLiveBase(BaseModel):
    state: HealthLiveStatus = Field(default=HealthLiveStatus.LIVE)


class HealthLivePublic(HealthLiveBase):
    pass
