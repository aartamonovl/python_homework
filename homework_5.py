# Домашнее задание Семинар 5* (сдавать только к семинару 5!)

def SwitchTask():
    taskNum = int(input("Введите номер задачи из домашней работы: "))
    while taskNum != 0:
        if taskNum == 26:
            Task26()
        elif taskNum == 28:
            Task28()
        else:
            print("Задачи с таким номером не задавали. Введите правильный номер задачи.")
        taskNum = int(input("Если все проведено, введите 0.\nВведите номер задачи из домашней работы: "))

# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def Task26():
    while True:
        a = int(input("Введите число А: "))
        b = int(input("Введите степень, в которую необходимо возвести число А: "))
        if a != 0:
            print(RecDegree(a, b))
        else:
            print("0 в любой степени = 0. Неопределенность не рассматривается.")
            break

def RecDegree(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1 / (a * RecDegree(a, -b - 1))
    else:
        return a * RecDegree(a, b - 1)

# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

def Task28():
    while True:
        a = int(input("Введите число a > 0: "))
        b = int(input("Введите число b > 0: "))
        if a > 0 and b > 0:
            res = Sum(a, b)
            print(res)
        else:
            break

def Sum(a, b):
    if b == 0:
        return a
    else:
        return Sum(a+1, b-1)

SwitchTask()