import json
import enemies_list
from Wizard import Wizard


def start():
    print_header()
    start_game_loop()


def print_header():
    print('-------------------------')
    print('     WIZARD GAME APP     ')
    print('-------------------------')


def start_game_loop():
    hero = Wizard('Wololo')

    while True and enemies_list.get_enemies():
        enemy = enemies_list.get_enemy()
        print('The wizard {} has level {}'.format(
            hero.get_name(), hero.get_level()))
        print('The wizard {} sees a {}, level {}.'.format(
            hero.get_name(), enemy.get_name(), enemy.get_level()), end='\n\n')
        user_command = str.strip(
            input('Do you [a]ttack, [r]un away or [l]ook around? ')
        )

        if user_command.lower() == 'a':
            hero_wins = hero.attack(enemy)
            if (hero_wins):
                hero.gain_level(enemy.get_level())
                enemies_list.delete_enemy(enemy)
                print('The wizard {} has been triuphant over {}'.format(
                    hero.get_name(), enemy.get_name()), end='\n\n')
            else:
                print('The wizard {} lost and had to hide to regain energy'.format(
                    hero.get_name()), end='\n\n')
                hero.reduce_level(enemy.level)
                hero.hide()
        elif user_command.lower() == 'r':
            print('The wizard {} ran away'.format(hero.get_name()))
        elif user_command.lower() == 'l':
            enemies_list.print_all()
        else:
            break


if __name__ == "__main__":
    start()
