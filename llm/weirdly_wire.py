from llm.agents.factory import AgentFactory, AgentPersona


class WeirdlyWire:
    def rewire_message(
        self, text_data: str, persona: AgentPersona = AgentPersona.FUNNY
    ):
        return (
            AgentFactory()
            .make_agent(persona)
            .get_answer(text_data, default=persona.default_message)
        )
