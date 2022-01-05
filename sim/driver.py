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
    pass#env = 

    # # days or cycles defined in the simulation
    # # several events happen between alliances 
    # def day(self):

    #     #step 1: choose which alliances are interacting
    #     interactions = self.create_interactions()
        
    #     #step 2: change alliances based on result of each interaction
    #     for interaction in interactions:
    #         alliance_choices = interaction.determine_choice_of_each_alliance()
    #         new_alliance_groupings = interaction.outcome()
    #         for alliance in interaction:
    #             self.alliances.remove(alliance)
    #         self.alliances.extend(new_alliance_groupings)
            