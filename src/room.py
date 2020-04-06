# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        if items == None:
            self.items = []
        else:
            self.items = items

    def print_room(self):
        wrapper = textwrap.TextWrapper(width=80)
        description = wrapper.wrap(text=self.description)
        print(''.join((self.name, '\n\n')))
        for s in description:
            print(s)
        print('\n')

    def print_items(self):
        if len(self.items) >= 1:
            print(f'The {self.name.lower()} contains:')
            for i in self.items:
                print(i.name)
            print('\n')
        else:
            print(f'The {self.name.lower()} is empty\n')
