# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, inventory=[]):
        self.name = name
        self.location = location
        self.inventory = []

    def __str__(self):
        return f'Player: {self.name}, Location: {self.location}'

    def move(self, entry, item):
        self.location = entry
        self.inventory.append(item)
        print(self.__str__())

    def inventory(self):
        for items in inventory:
            return print(items)
