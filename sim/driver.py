# imports
from typing import Counter
import environment_types
import alliance_types
import agent_types

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

print(type_of_agents)
print(type_of_alliances)

win_condition = False # arbitrary win condition that can be defined in its
                      # own function and varied in sim_settings
current_day = 0 #init phase

alliances = []

for i in range(num_agents):
    # assume all agents and alliances are basic for now
    # consider how to handle the nonhomogeneous case of agents
    # and alliances
    if type_of_agents == 'basic' and type_of_alliances == 'basic' :
        counter = 0
        agent_name = str(counter)
        # init with name, strength
        agent = BasicAgent(agent_name, 10*random.random())
        alliance = BasicAlliance(agent)
        alliances.append(alliance)
        counter += 1
    else:
        print('err000 agents and alliances are not basic unhandled exception')

#for i in alliances:
 #   pprint(vars(i))

if type_of_environment == 'basic':
    env = BasicENV(alliances)
else:
    print('err001 environment is not basic unhandled exception')

current_day += 1
#debug
print('active alliances day: ', current_day)

# actual epoch cycle
while not win_condition or current_day <= num_days:

    # create the interaction groups
    interaction_groups = env.group_all()
    # interaction changes the list of alliances therefore reset it and update
    alliances = []

    for interact_set in interaction_groups:
        # is a set and can be one or more alliances
        resultant_alliances = env.interact(interact_set)
        # add to new list of alive alliances
        for alli in resultant_alliances:
            alliances.append(alli)

    current_day += 1 # day is now done

    #debug
    print('active alliances day: ', current_day)
    print(alliances)
            