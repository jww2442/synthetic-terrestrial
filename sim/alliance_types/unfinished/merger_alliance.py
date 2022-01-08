from generic_alliance import Alliance

class mergable_alliance(Alliance):
    def __init__(self, first_member):
        super(self, first_member)

    #handles the case in which two alliances merge
    def merge(self, other_alli):
        self.aggression = (self.aggression * len(self.members) + other_alli.aggression * len(other_alli.members))/(len(self.members)+len(other_alli.members))
        # consider defining a strength function
        self.strength += other_alli.strength
        self.members.extend(other_alli.members)

    def choose_collective_action(possible_choices):
        if('merge' in possible_choices):
            return 'merge'
        pass