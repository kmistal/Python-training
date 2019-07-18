import random
from Creature import Creature
from Wizard import Wizard


enemies = [
    Creature('Toad', 1),
    Creature('Alligator', 5),
    Creature('Bear', 20),
    Creature('Toad', 1),
    Creature('Alligator', 5),
    Creature('Bear', 20),
    Creature('Habahabahaba', 200),
    Creature('Chujemuje', 123),
    Creature('Toad', 1),
    Creature('Alligator', 5),
    Creature('Bear', 20),
    Creature('Toad', 1),
    Creature('Alligator', 5),
    Creature('Bear', 20),
    Creature('Habahabahaba', 200),
    Creature('Chujemuje', 123),
    Wizard('Grześ', 1500),
]


def get_enemies():
    global enemies
    return enemies


def get_enemy():
    enemies = get_enemies()
    index = random.randrange(0, len(enemies))
    return enemies[index]


def print_all():
    for enemy in get_enemies():
        enemy.print_name()


def delete_enemy(enemy):
    enemies = get_enemies()
    enemies.remove(enemy)
