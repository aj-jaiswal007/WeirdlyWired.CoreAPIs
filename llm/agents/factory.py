from llm.enums import AgentPersona
from llm.agents.base import BaseAgent
from llm.agents.funny import FunnyAgent
from llm.agents.polite import PoliteAgent


PERSONA_AGENT_MAP = {
    AgentPersona.FUNNY: FunnyAgent,
    AgentPersona.POLITE: PoliteAgent,
}


class AgentFactory:
    @staticmethod
    def make_agent(persona: AgentPersona) -> BaseAgent:
        if persona in PERSONA_AGENT_MAP:
            return PERSONA_AGENT_MAP[persona]()

        raise ValueError(f"Invalid persona: {persona}")
