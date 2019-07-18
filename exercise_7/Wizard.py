import random
from time import sleep
from Creature import Creature


class Wizard(Creature):
    def __init__(self, name, level=1):
        super().__init__(name, level)

    def attack(self, enemy):
        wizard_roll = self.get_attack_points()
        enemy_roll = enemy.get_defensive_points()

        print('The wizard {} rolled {}'.format(self.name, wizard_roll))
        print('The {} rolled {}'.format(enemy.get_name(), enemy_roll))

        return wizard_roll >= enemy_roll

    def get_attack_points(self):
        return random.randrange(1, 100) * self.level

    def gain_level(self, level):
        self.level += level

        return self.level

    def reduce_level(self, level):
        if (self.level - level <= 1):
            self.level = 1
        else:
            self.level -= level

        return self.level

    def hide(self):
        sleep(3)
