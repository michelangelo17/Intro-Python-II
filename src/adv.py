from room import Room
from player import Player
from item import Item
# Declare all the items
item = {
    'sword': Item('sword', 'an average looking sword'),
    'lettuce': Item('lettuce', 'fresh lettuce'),
    'axe': Item('axe', 'a typical wood axe'),
    'coins': Item('coins', 'coins from the old kingdom')
}

# Declare all the rooms

room = {
    'outside':  Room('Outside Cave Entrance',
                     'North of you, the cave mount beckons',
                     [item['sword'], item['lettuce']]),

    'foyer':    Room('Foyer',
                     'Dim light filters in from the south. Dusty passages run north and east.',),

    'overlook': Room('Grand Overlook',
                     'A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.',
                     [item['coins']]),

    'narrow':   Room('Narrow Passage',
                     'The narrow passage bends here from west to north. The smell of gold permeates the air.'),

    'treasure': Room('Treasure Chamber',
                     'You\'ve found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.',
                     [item['axe']]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# Make a new player object that is currently in the 'outside' room.

name = input('Please enter your name: ')

player1 = Player(name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

instructions = ''.join(('INSTRUCTIONS: \n',
                        'Press \'n\' to go North, \'e\' to go East, \'s\' to go South, or \'w\' to go West!\n',
                        'To take an item, type \'take [item_name]\' or \'get [item_name]\'\n',
                        'To drop an item, type \'drop [item_name]\'\n',
                        'To check your inventory, type \'i\' or \'inventory\'\n\n\n'))

print(''.join(('\nREADY PLAYER ONE\n\n\n',
               f'Welcome to the adventure game {player1.name}!\n\n\n',
               instructions)))

player1.current_room.print_room()
player1.current_room.print_items()

while True:
    command = input('--->  ')
    if command == 'q':
        print('\nGoodbye!\n')
        exit(0)
    try:
        player1.action(command.split())
    except Exception as e:
        print(''.join((f'\n{e}\n\n', instructions)))


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters 'q', quit the game.
