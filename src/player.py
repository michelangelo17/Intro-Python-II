# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, initial_room, items=None):
        self.name = name
        self.current_room = initial_room
        if items == None:
            self.items = []
        else:
            self.items = items

    def move(self, dir):
        if getattr(self.current_room, f'{dir}_to'):
            self.current_room = getattr(self.current_room, f'{dir}_to')
            print('\nMove to:')
            self.current_room.print_room()
            self.current_room.print_items()
        else:
            print('\nNo path lies that direction.\n')

    def take(self, item):
        for i in self.current_room.items:
            if i.name == item:
                self.items.append(i)
                self.current_room.items.remove(i)
                i.on_take()
                self.current_room.print_items()
                break
        else:
            print(f'There is no {item} in the {self.current_room.name}\n')

    def drop(self, item):
        for i in self.items:
            if i.name == item:
                self.items.remove(i)
                self.current_room.items.append(i)
                i.on_drop()
                self.current_room.print_items()
                break
        else:
            print(f'You do not have {item} in your inventory.\n')

    def inventory(self):
        print('You are carrying:')
        if len(self.items) > 0:
            for i in self.items:
                print(i.name)
        else:
            print('Nothing!')

    def action(self, commands):
        if len(commands) == 1:
            if commands[0] in ('n', 'e', 's', 'w'):
                self.move(commands[0])
            elif commands[0] == 'i' or commands[0] == 'inventory':
                self.inventory()
            else:
                raise ValueError('Unrecognised command!')
        elif len(commands) == 2:
            if commands[0] == 'take' or commands[0] == 'get':
                self.take(commands[1])
            elif commands[0] == 'drop':
                self.drop(commands[1])
            else:
                raise ValueError('Unrecognised command!')
        else:
            raise IndexError('Unrecognised command!')
