from datetime import datetime
from enum import Enum
from typing import Annotated
from uuid import uuid4

from beanie import Document, Indexed
from pydantic import UUID4, BaseModel, ConfigDict, Field, Strict
from app.common.models.aimodels_model import AIModel
from app.common.models.aimodels_model import AssistantType


class QuestionCategory(str, Enum):
    PROJECTGOAL: "Projektzielklärung"
    RESSOURCES: "Ressourcenanalyse"
    CHALLENGES: "Hindernisse identifizieren"
    STRATEGY: "Strategie entwickeln"
    REFLECTION: "Reflexion und Anpassung"
    MOTIVATION: "Motivationsstärkung"
    MANAGEMENT: "Zeitmanagement und Ressourcenplanung"


class CheckListItem(BaseModel):
    checked: bool = Field(default=False)
    content: str | None = Field(default=None, max_length=2000)
    category: QuestionCategory
    note: str | None = Field(default=None, max_length=2000)


class TemplateBase(BaseModel):
    userId: UUID4
    title: str = Field(max_length=200)
    prompt: str | None = Field(default=None, max_length=2000)


class Template(Document, TemplateBase):
    id: Annotated[UUID4, Indexed(), Strict(False)] = Field(
        default_factory=uuid4, alias="_id", serialization_alias="id"
    )
    check_list: list[CheckListItem] = Field(default_factory=[])
    ai_model: AIModel
    deleted: datetime | None = None
    created: datetime = Field(default=datetime.now())

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                # TODO
            }
        }
    )

    class Settings:
        keep_nulls = True
        name = "templates_collection"


class TemplateCreate(TemplateBase):
    assistant_type: AssistantType


class TemplateUpdate(BaseModel):
    check_list: list[CheckListItem]
