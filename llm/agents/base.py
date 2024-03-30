from abc import ABC
from langchain_core.language_models.chat_models import BaseChatModel
from common.logger import logger


class BaseAgent(ABC):
    # To be defined by the child class
    llm: BaseChatModel = None  # type: ignore
    prompt_template: str = None  # type: ignore

    def __str__(self) -> str:
        # Return class name
        return self.__class__.__name__

    def get_answer(self, user_input: str, default: str) -> str:
        """Make a call to the llm to get the response for the user input

        Args:
            user_input (str): User input.
            default (str): Default response in case of error.

        Returns:
            str: LLM response.
        """
        logger.info(
            f"Making llm call on llm:{self.llm}, agent:{self}, with user input:{user_input}"
        )
        try:
            response = self.llm.invoke(
                self.prompt_template.format(user_input=user_input)
            )
            logger.info(f"Response from llm={response.content}")
            return response.content  # type: ignore

        except Exception as e:
            logger.exception(f"Error in making llm call: {e}")
            return default or user_input
