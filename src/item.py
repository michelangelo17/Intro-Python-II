class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'You have picked up: {self.name}\n')

    def on_drop(self):
        print(f'You have dropped: {self.name}\n')


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print('It is not wise to drop your source of light!')
