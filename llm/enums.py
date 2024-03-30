from enum import Enum


class AgentPersona(str, Enum):
    FUNNY = "funny"
    POLITE = "polite"

    @property
    def default_message(self):
        return f"I feel {self.value} today!"
