# imports
import environment_types
import alliance_types
import agent_types

#from environments.env import Environment
#from agents.agent import Agent
#from alliances.alliance import Alliance

import random
from pprint import pprint
import json

from agent_types.basic_agent import BasicAgent
from alliance_types.basic_alliance import BasicAlliance
from environment_types.basic_env import BasicENV

# sim_settings.json allows for easy change of game settings without 
# changing info in source code. we can change the type of env, allowed
# types of agents, numDays, etc.

# we import the file and assign variables accordingly. enventually, this will
# be done using a GUI.
settingsFile = open('sim/sim_settings.json')
settings = json.load(settingsFile)

# setting variables
num_days = settings['numberOfDaysInSim']
num_agents = settings['numberOfTotalAgents']
type_of_agents = settings['agentType']
type_of_environment = settings['environmentType']
type_of_alliances = settings['allianceType']

alliances = []

for i in range(num_agents):
    # assume all agents and alliances are basic for now
    # consider how to handle the nonhomogeneous case of agents
    # and alliances
    if type_of_agents == 'basic' and type_of_alliances == 'basic' :
        agent = BasicAgent(10*random.random(), 20*random.random())
        alliance = BasicAlliance(agent)
        alliances.append(alliance)
    else:
        print('err000 agents and alliances are not basic unhandled exception')

#for i in alliances:
 #   pprint(vars(i))

if type_of_environment == 'basic':
    env = BasicENV(alliances)
else:
    print('err001 environment is not basic unhandled exception')

# actual epoch cycle
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
            