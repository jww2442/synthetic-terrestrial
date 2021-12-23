from interaction_types.generic_interaction import Interaction

class Environment:

    def __init__(self, alliances):
        self.alliances = alliances

    # days or cycles defined in the simulation
    # several events happen between alliances 
    def day(self):

        interactions = self.create_interactions()
        #step 1: choose which alliances are interacting
        interact_sets = self._create_encounter_pairs()
        
        #step 2: perform interaction b/w alliances
        self._interact(interact_sets)


    #TODO: delete this and change to create_interactions()
    def create_interaction(self):
        interactions = []
        alliances_copy = self.alliances.copy()
        alliances_copy.shuffle()
        for i in range(0, len(alliances_copy), 2):
            interactions.append(Interaction([alliances_copy[i], alliances_copy[i+1]]))

        return interactions