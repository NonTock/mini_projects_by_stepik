import random
from time import sleep
from colorama import Fore, Style, init
init(autoreset=True)

def correct_digit(num):                               #Проверка на правильность введенного значения
    while True:
        if num.isdigit():
            if 0 <= int(num) <= 100:
                return int(num)
        else:
            num = (input(system_msg+"Давайте всё же введем число от 1 до 100:"))

def find_game(num):
    counter = 0                                       #Счётчик попыток
    random_number = random.randint(1, 100)      #Создание случайного числа в диапазоне от 1 до 100 включительно
    num = correct_digit(num)
    while num != random_number:                       #Проверка больше/меньше и поиск результата
        if num > random_number:
            counter += 1
            print(system_msg+f"Ваше число: {num} больше загаданного")
            num = input(system_msg + "Давайте ещё число:")
        elif num < random_number:
            counter += 1
            print(system_msg+f"Ваше число: {num} меньше загаданного, давайте ещё:")
            sleep(0.5)
            num = input(system_msg+"Давайте ещё число:")
        num = correct_digit(num)
    else:
        counter += 1
        print(win_msg+"В точку, поздравляем!")
        print(win_msg+f"Ваше количество попыток: {counter}")
system_msg = Style.BRIGHT+Fore.LIGHTBLUE_EX
win_msg = Style.BRIGHT+Fore.LIGHTGREEN_EX
print(system_msg+'Добро пожаловать в "Угадай Число" by NonTock')
sleep(1)
choose = input(system_msg+"Хотите ли сыграть 'Да'/'Нет':").lower()
while choose != "да":
    if choose == "нет":
        print(system_msg+"Очень жаль, надеемся что ещё поиграем!")
        break
    choose = input(system_msg+"Если передумаете вы всегда можете написать 'да'")
else:
    tryin = input(system_msg+"Введите число строго от 1 до 100:")
    find_game(tryin)
    while True:                                                                    #Бесконечный цикл после окончания раунда игры, с последующим запуском новой
        tryin = input(system_msg+"Если хотите сыграть ещё, введите новое число или напишите 'Хватит':").lower()
        if tryin == "хватит":
            print(system_msg + "Очень жаль, надеемся что ещё поиграем!")
            break
        find_game(tryin)
