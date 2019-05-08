import random

print('-----------------------------')
print('     GUESS THE NUMBER APP    ')
print('-----------------------------')

expected_number = random.randrange(100)
guessed_number = None

while guessed_number != expected_number:
    guessed_number = input('GUESS NUMBER BETWEEN 0 AND 100: ')
    guessed_number = int(guessed_number)

    if guessed_number == expected_number:
        print('Yes! You\'ve got it. The number was ' + str(expected_number))
        break
    elif guessed_number < expected_number:
        print('Sorry but ' + str(guessed_number) +
              ' is smaller than the number')
    elif guessed_number > expected_number:
        print('Sorry but ' + str(guessed_number) +
              ' is bigger than the number')
