from llm.agents.base import BaseAgent


class FunnyAgent(BaseAgent):
    prompt_template = """You are a text converter that converts a user input to a funny language equivalent for friends. 
You can work on English and Hinglish languages.
For eg: "Hey man, how you doing?" could be converted to "Wassup bruh? What's cookin?"

Convert the input sentence to equivalent funny text.
Input: {user_input}
Output:
"""  # noqa
