class Agent:
    
    def Agent(self, strength_dist, aggr_dist):
        
        self.strength = strength_dist.sample()
        
        self.aggression = aggr_dist.sample()