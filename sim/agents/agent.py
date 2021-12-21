class Agent:
    
    def __init__(self, name, strength_dist, aggr_dist):
        
        self.name = name

        self.strength =  strength_dist#.sample()
        
        self.aggression = aggr_dist#.sample()