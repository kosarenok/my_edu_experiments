"""
Задача 1 (3 балла): 
Написать функцию, принимающую число от 0 до 1000,
определяющую, является ли это число простым и возвращающую True, если да,
False если нет. Использовать эту функцию в программе, которая просит пользователя
ввести число с клавиатуры и выводит в консоль результат. 
Встроенными библиотеками пользоваться нельзя.
"""

def find_simple_number():
    try:
        number=int(input("Введите число от 1 до 1000:"))
    except ValueError:
        return print("Число, которое вы ввели имеет неверный тип данных, пожалуйста введите натуральное число.")
    if not 1 < number <= 1000:
        return print("Число, которое вы ввели не в диапозоне")
    else:
        count = 0
        for i in range(1, number+1):
            if i % number == 0:
                count += 1
        if count == 2:
            return print(True)
        else:
            return print(False)

find_simple_number()



