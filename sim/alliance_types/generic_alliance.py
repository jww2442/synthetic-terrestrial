from abc import ABC, abstractmethod


class Alliance(ABC):

    #constructor, accepts first_member of type agent
    def __init__(self, first_member):
        self.members = [first_member]

    @abstractmethod
    def choose_collective_action(possible_choices): #implemented in descendents
        pass