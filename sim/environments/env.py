class Environment:

    def __init__(self, alliances):
        self.alliances = alliances

    def day(self):
        #step 1: choose which alliances are interacting
        interact_sets = self._create_encounter_pairs()
        
        #step 2: perform interaction b/w alliances
        self._interact(interact_sets)

    def _create_encounters_pairs(self):
        pairs = []

        alliances_copy = self.alliances.copy()
        alliances_copy.shuffle()
        for i in range(0, len(alliances_copy), 2):
            pairs.append((alliances_copy[i], alliances_copy[i+1]))

        return pairs


    def _interact(interact_sets):
        for group_of_alliances in interact_sets:
            if(True):
                _fight(group_of_alliances)