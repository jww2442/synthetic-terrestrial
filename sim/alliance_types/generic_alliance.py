from abc import ABC, abstractmethod #might make this class abstract


class Alliance(ABC):

    #constructor, accepts first_member of type agent
    def __init__(self, first_member):
        self.members = [first_member]
        self.strength = first_member.strength
        self.aggression = first_member.aggression

    @abstractmethod
    def choose_collective_action(possible_choices): #implemented in descendents
        pass      