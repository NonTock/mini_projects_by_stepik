import random

def correct_digit(num):                                         #Проверка на правильность введенного значения
    while True:
        if num.isdigit():
            if 0 < int(num) <= 100:
                return int(num)
        else:
            num = (input("Давайте всё же введем число от 1 до 100:"))

def find_game(num):
    counter = 0                                                                     #Счётчик попыток
    random_number = random.randint(1, 100)                                    #Создание случайного числа в диапазоне от 1 до 100 включительно
    num = correct_digit(num)
    while num != random_number:                                                     #Проверка больше/меньше и поиск результата
        if num > random_number:
            counter += 1
            num = input(f"Ваше число:{num} больше загаданного, давайте ещё:")
        elif num < random_number:
            counter += 1
            num = input(f"Ваше число:{num} меньше загаданного, давайте ещё:")
        num = correct_digit(num)
    else:
        counter += 1
        print("В точку, поздравляем!")
        print(f"Ваше количество попыток: {counter}")
print('Добро пожаловать в "Угадай Число" by NonTock')
choose = input("Хотите ли сыграть 'да'/'нет':")
while choose != "да":
    choose = input("Если передумаете вы всегда можете написать 'да'")
else:
    tryin = input("Введите число строго от 1 до 100:")
    find_game(tryin)
    while True:                                                                    #Бесконечный цикл после окончания раунда игры, с последующим запуском новой
        tryin = input("Если хотите сыграть ещё, введите новое число:")
        find_game(tryin)
