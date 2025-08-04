import os
from openai import OpenAI
from app.chats.schemas import ChatMessage, ChatCompletionRequest, ChatCompletionResponse

class OpenAIChatClient:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def create_chat_completion(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        response = self.client.beta.chat.completions.parse(
            model=request.model,
            messages=[msg.model_dump() for msg in request.messages],
            max_tokens=request.max_tokens
        )
        response_dict = response.model_dump()
        response_dict["choices"] = [
            ChatMessage(**choice["message"]) for choice in response_dict["choices"]
        ]
        return ChatCompletionResponse(**response_dict)


def ask():
    print("Welcome to the OpenAI Chat Client!")
    while True:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("Please set the OPENAI_API_KEY environment variable.")
        client = OpenAIChatClient(api_key)
        prompt = input("Enter your prompt (or 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        request = ChatCompletionRequest(
            model="gpt-4o-mini",
            messages=[
                ChatMessage(role="system", content="You are a helpful assistant."),
                ChatMessage(role="users", content=prompt),
            ],
            max_tokens=1000
        )

        response = client.create_chat_completion(request)
        with open("plan_mvp.md", "w", encoding="utf-8") as file:
            file.write(response.choices[0].content)

        print(response.model_dump_json(indent=2))  # This will print the response in a formatted JSON style