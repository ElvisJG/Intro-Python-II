# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f'Player: {self.name}, Location: {self.location}'

    def move(self, entry):
        self.location = getattr(self.location, f'{entry}_to')
        print(self.__str__())
