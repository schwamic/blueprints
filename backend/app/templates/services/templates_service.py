from abc import abstractmethod

from fastapi import HTTPException

from app.common.models.aimodels_model import AssistantType
from app.common.clients.openai_client import OpenAIClient
from app.templates.models.templates_model import Template, TemplateCreate
from app.users.models.users_model import User


class AIChat:
    @abstractmethod
    def send(self, prompt: str):
        pass


class AIClient:
    @abstractmethod
    def create_chat(self, assistant_type: AssistantType) -> AIChat:
        pass


class TemplatesService:
    def __init__(self, ai_client: AIClient):
        self.ai_client = ai_client

    async def create_template(self, template_create: TemplateCreate) -> Template:
        user = User.get(template_create.user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        ai_chat = self.ai_client.create_chat(template_create.assistant_type)
        response = ai_chat.send(template_create.prompt)
        template = Template(
            user_id=template_create.user_id,
            title=template_create.title,
            prompt=template_create.prompt,
            check_list=response.json(),
            ai_model=ai_chat.model,
        )
        created_template = await template.insert()
        return created_template

    async def get_template(self, template_id: str) -> Template:
        template = await Template.get(template_id)
        if template is None:
            raise HTTPException(status_code=404, detail="Template not found")
        return template


templatesService = TemplatesService(OpenAIClient())
