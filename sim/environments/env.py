class Environment:

    # init the environment
    def __init__(self, alliances):
        # list of alliance objects
        self.alliances = alliances

    # days or cycles defined in the simulation
    # several events happen between alliances 
    def _day(self):
        #step 1: choose which alliances are interacting
        interact_sets = self._create_encounter_pairs()
        
        #step 2: perform interaction b/w alliances
        self._interact(interact_sets)

    # randomly select pairs of alliances and store them into a data structure
    # only two alliances can intereact for now
    def _create_encounters_pairs(self):
        pairs = []

        alliances_copy = self.alliances.copy()
        alliances_copy.shuffle()
        for i in range(0, len(alliances_copy), 2):
            pairs.append((alliances_copy[i], alliances_copy[i+1]))

        return pairs # where pairs is a list of 1 by 2 vectors


    # for initial release, agents always fight therefore alliances.alliance.will_fight is always true
    def _interact(self, interact_sets):
        for group_of_alliances in interact_sets:
            if(group_of_alliances[0].will_fight() or group_of_alliances[1].will_fight()):  # if either will fight
                if (group_of_alliances[0].fight() < group_of_alliances[1].fight()):
                    # alliance[1] wins
                    self._kill(group_of_alliances[0])
                else:
                    # alliance[0] wins
                    self._kill(group_of_alliances[1])
            # if neither will fight then do what?
    
    # kill function that removes an alliance from the data structure
    def _kill(self, dead_alliance):
        self.alliances.remove(dead_alliance)
