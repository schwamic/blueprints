from langchain_openai import ChatOpenAI
from langchain.schema.messages import AIMessage, HumanMessage
from app.common.core.settings import settings
from enum import Enum


class Assistant(str, Enum):
    QUESTIONER = "questioner"
    INSTRUCTOR = "instructor"


class OpenAIClient:
    def __init__(self):
        self.chat = None
        self.instructions = {
            "questioner": "Ask 5 to 15 questions.",
            "instructor": "Provide 5 to 15 instructions.",
        }

    def create_chat(self, assistant: Assistant):
        if assistant == Assistant.QUESTIONER:
            return Chat(self.instructions.questioner)
        elif assistant == Assistant.INSTRUCTOR:
            return Chat(self.instructions.instructor)
        else:
            raise ValueError("Invalid chat type")


class Chat:
    def __init__(self, instructions: str):
        self.ai_message = AIMessage(content=[{"type": "text", "text": instructions}])
        self.chat = ChatOpenAI(
            openai_api_key=settings.OPENAI_API_KEY,
            model_name="gpt-4o",
            model_kwargs={"top_p": 0, "seed": 42},
            temperature=0,
        )

    def send(self, prompt: str):
        response = self.client.invoke([self.ai_message, HumanMessage(content=prompt)])
        return response.content


openai_client = OpenAIClient()
