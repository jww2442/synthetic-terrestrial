from generic_env import Environment
import numpy as np


class BasicENV(Environment):

    def group_all(self):
        interaction_groups = []
        alliances_copy = self.alliances.copy()
        alliances_copy.shuffle()
        for i in range(0, len(alliances_copy), 2):

            interaction_groups.append({alliances_copy[i], alliances_copy[i+1]})

        return interaction_groups #list of sets

    def interact(group):

        decisions = set()
        for alliance in group:
            decisions.add({alliance.decide(group - alliance)})

        if(decisions.contains('fight')): 
            winner = None
            max_str = -np.inf
            for alliance in group:
                str = alliance.get_strength()
                if(str > max_str):
                    max_str = str
                    winner = alliance

            return {winner} #no absorbing other alliances yet

        elif(len(decisions) == 1 and decisions.contains('merge')): #all alliances want to merge
            print('err9422(we are not ready to handle merging)')
            exit()
        elif(decisions.contains('no_act')):
            return group
        else: 
            print('err4932')
            exit()
