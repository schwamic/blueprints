import json

from langchain.schema.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI

from app.common.core.settings import settings
from app.common.models.aimodels_model import AssistantType, AIModel
from app.templates.services.templates_service import AIClient, AIChat


INSTRUCTIONS_JSON_FILE_PATH = "../core/ai_instructions.json"
TOP_P = 0
SEED = 42
TEMPERATURE = 0
MODEL = "gpt-4o"


class OpenAIClient(AIClient):
    def __init__(self):
        with open(INSTRUCTIONS_JSON_FILE_PATH, "r") as file:
            self.instructions = json.load(file)

    def create_chat(self, assistant_type: AssistantType) -> AIChat:
        ai_model = AIModel(
            assistant_type=assistant_type,
            name=MODEL,
            seed=SEED,
            temperature=TEMPERATURE,
            top_p=TOP_P,
        )
        return GPTChat(ai_model, self.instructions[assistant_type])


# refactor:
# https://platform.openai.com/docs/guides/structured-outputs/introduction
class GPTChat(AIChat):
    def __init__(self, model: AIModel, instructions: str):
        self.model = model
        self.ai_message = AIMessage(content=[{"type": "text", "text": instructions}])
        self.chat = ChatOpenAI(
            openai_api_key=settings.OPENAI_API_KEY,
            model_name=self.model.name,
            model_kwargs={"top_p": self.model.top_p, "seed": self.model.seed},
            temperature=self.model.temperature,
        )

    def send(self, prompt: str):
        response = self.chat.invoke([self.ai_message, HumanMessage(content=prompt)])
        return response.content

    @property
    def model(self):
        return self.model


openai_client = OpenAIClient()
