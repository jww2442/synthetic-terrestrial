from generic_alliance import Alliance

class BasicAlliance(Alliance):

    def __init__(self, first_member):
        super(first_member)

    def choose_collective_action(possible_choices):
        if(possible_choices.contains('fight')):
            return 'fight'

        else: 
            print('err413491')
            exit() #always fight

    # strength fx defined as average of each agent in the alliance
    def get_strength(self): 
        str = 0
        for member in self.members:
            str += member.strength

        str /= len(self.members)
        
        return str