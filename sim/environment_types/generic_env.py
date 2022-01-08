from abc import ABC, abstractmethod

class Environment(ABC):

    def __init__(self, alliances):
        self.alliances = alliances #list of alliance objects
        
    @abstractmethod
    def group_all(self):
        pass

    @abstractmethod
    def interact(group):
        pass

    