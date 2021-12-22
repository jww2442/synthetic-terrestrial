from environments.env import Environment
from agents.agent import Agent
from alliances.alliance import Alliance

import random
from pprint import pprint


num_agents = 20
alliances = []

for i in range(num_agents):
    agent = Agent(10*random.random(), 20*random.random())
    alliance = Alliance(agent)
    alliances.append(alliance)

for i in alliances:
    pprint(vars(i))


env = Environment(alliances)



num_days = 50

for i in range(num_days):
    env = 