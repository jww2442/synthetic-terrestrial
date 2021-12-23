import random

class Alliance:

    #constructor, accepts first_member of type agent
    def __init__(self, first_member):
        self.members = [first_member]
        self.strength = first_member.strength
        self.aggression = first_member.aggression

    def merge(self, other_alli):
        self.aggression = (self.aggression * len(self.members) + other_alli.aggression * len(other_alli.members))/(len(self.members)+len(other_alli.members))
        # consider defining a strength function
        self.strength += other_alli.strength
        self.members.extend(other_alli.members)
        
    # determine if the alliance will fight
    def will_fight(self):

        if(random.random() < self.aggression):
            return True
        else:
            return False

    # initiate a fight, return strength value
    # winner and consequences are determined based on comparing two alliance's fight() 
    # in env.py in the interact fx
    def fight(self): #involved_alliances was in arg, not needed
        # determined by a strength function as in merge and init
        return self.strength