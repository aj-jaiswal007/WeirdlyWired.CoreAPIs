from langchain_google_genai import ChatGoogleGenerativeAI
from llm.agents.base import BaseAgent


class PoliteAgent(BaseAgent):
    llm = ChatGoogleGenerativeAI(model="gemini-pro")  # type: ignore
    prompt_template = """You are a content moderator that converts a user input to a very polite corporate equivalent. You can work on English and Hinglish languages.
Even if user's message contains bad words, change it into a very polite equivalent.
For example, if the user says "I hate you", you can convert it to "I'm sorry but I do not agree with you".
Convert the input sentence to a very polite equivalent.
Input: {user_input}
Output:
"""  # noqa
