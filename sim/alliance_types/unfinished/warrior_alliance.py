from generic_alliance import Alliance

class warrior_clan(Alliance):

    def __init__(self, first_member):
        super(self, first_member)
        self.strength = first_member.strength
        self.aggression = first_member.aggression

    def choose_collective_action(possible_choices):
        if(possible_choices.contains('fight')):
            return 'fight'
        elif(possible_choices.contains('no_action')):   
            return 'no_action'
        else:
            print('err9041')
            exit()

