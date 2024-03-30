from langchain_google_genai import ChatGoogleGenerativeAI
from llm.agents.base import BaseAgent


class FunnyAgent(BaseAgent):
    llm = ChatGoogleGenerativeAI(model="gemini-pro")  # type: ignore
    prompt_template = """You are a text converter that converts a user input to a funny street language equivalent. You can work on English and Hinglish languages.
For eg: "Hey man, how you doing?" could be converted to "Wassup dawg? What's cookin?"

Convert the input sentence to street language.
Input: {user_input}
Output:
"""  # noqa
