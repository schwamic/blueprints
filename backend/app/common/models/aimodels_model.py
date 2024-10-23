from enum import Enum

from pydantic import BaseModel, ConfigDict


class AssistantType(Enum):
    QUESTIONER = "questioner"
    INSTRUCTOR = "instructor"


class AIModel(BaseModel):
    name: str
    assistant_type: AssistantType
    top_p: float
    seed: int
    temperature: float

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "gpt-4o-2024-08-06",
                "assistant_type": "questioner",
                "top_p": "0.31",
                "seed": "42",
                "temperature": "0.27",
            }
        }
    )
