import os
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.chat import chat
from autogen_ext.models.openai import OpenAIChatCompletionClient


def main() -> None:
    """Run a simple AutoGen conversation using the OPENAI_API_KEY env var."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing. Set it before running the demo.")

    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        api_key=api_key,
    )

    assistant = AssistantAgent("assistant", model_client=model_client)
    user = UserProxyAgent("tester")

    prompt = "Bonjour AutoGen. Resumes en une phrase ce qu'est AutoGen."
    result = chat(user, assistant, prompt)

    print("\n=== Assistant response ===")
    if result.messages:
        print(result.messages[-1].content)
    else:
        print("(no response received)")


if __name__ == "__main__":
    main()
