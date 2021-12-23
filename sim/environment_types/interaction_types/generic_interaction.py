class Interaction:
    def __init__(self, alliances):
        self.alliances = alliances
        self.possible_choices = ['fight']

    def determine_choice_of_each_alliance(self):
        all_alliance_choices = dict.fromkeys(self.alliances)

        for alli in self.alliances:
            decision = alli.choose_collective_action(self.possible_choices)
            all_alliance_choices.update({alli: decision})

        return all_alliance_choices

    def get_result_of_interaction(all_alliance_choices):

        for alli in all_alliance_choices:
            if(all_alliance_choices.get(alli) == 'fight'):
                return 'fight'

        print('err9313')
        exit()

    def fight():
        #TODO
        pass


