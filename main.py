from random import randint

from start_game_banner import run_screensaver

"""какой-то doc."""


def attack(char_name, char_class):
    """какой-то doc."""
    if char_class == 'warrior':
        damage = 5+randint(3, 5)
        return (f'{char_name} нанёс урон противнику равный {damage}')
    if char_class == 'mage':
        damage = 5+randint(3, 10)
        return (f'{char_name} нанёс урон противнику равный {damage}')
    if char_class == 'healer':
        damage = 5+randint(-3, -1)
        return (f'{char_name} нанёс урон противнику равный {damage}')
    return None


def defence(char_name, char_class):
    """какой-то doc."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return None


def special(char_name, char_class):
    """какой-то doc."""
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение «Выносливость {10}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {45}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита {40}»')
    return None


def start_training(char_name, char_class):
    """какой-то doc."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack, defence, special')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    """какой-то doc."""
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор').lower()
    return char_class


def main():
    """какой-то doc."""
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
