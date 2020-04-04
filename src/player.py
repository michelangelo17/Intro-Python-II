# Write a class to hold player information, e.g. what room they are in
# currently.

directions = {
    'n': {
        'go': 'n_to',
        'message': 'move North'
    },
    'e': {
        'go': 'e_to',
        'message': 'move East'
    },
    's': {
        'go': 's_to',
        'message': 'move South'
    },
    'w': {
        'go': 'w_to',
        'message': 'move West'
    },
}


class Player:
    def __init__(self, location):
        self.location = location

    def move(self, d):
        try:
            self.location = getattr(self.location, directions[d]['go'])
            print(directions[d]['message'].capitalize()+'!')
        except:
            print('You try to ' +
                  directions[d]['message'] + ' but there\'s nowhere to go!')
