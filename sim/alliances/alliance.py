import random

class Alliance:

    #constructor, accepts first_member of type agent
    def __init__(self, first_member):
        self.members = [first_member]
        self.strength = first_member.strength
        self.aggression = first_member.aggression

    def merge(self, other_alli):
        self.aggression = (self.aggression * len(self.members) + other_alli.aggression * len(other_alli.members))/(len(self.members)+len(other_alli.members))
        self.strength += other_alli.strength
        self.members.extend(other_alli.members)
        
    def will_fight(self):

        if(random.random() < self.aggression):
            return True
        else:
            return False