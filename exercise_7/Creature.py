import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_defensive_points(self):
        return random.randrange(1, 100) * self.level

    def get_level(self):
        return self.level

    def get_name(self):
        return self.name

    def print_name(self):
        print('Yeah, this is {}, {} level!'.format(
            self.name, self.level))
