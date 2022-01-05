from abc import ABC, abstractmethod #might make this class abstract



class Agent(ABC):
    
    def __init__(self, name):
        
        self.name = name
