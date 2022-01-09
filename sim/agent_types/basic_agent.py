import agent_types.generic_agent as ga


class BasicAgent(ga.Agent):

    def __init__(self, str):
        super()
        self.strength = str

    