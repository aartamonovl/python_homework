

def SwitchTask ():
    taskNum = int(input("Введите номер задачи из домашней работы: "))
    taskNumber = {
        2: TaskTwo(),
        4: TaskFour(),
        # 6: TaskSix(),
        # 8: TaskEight()
    }
    taskNumber.get(taskNum, "Нет такой задачи")

# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def TaskTwo ():
    num = str(input("Ввдите трехзначное число: "))
    if len(num) == 3:
        print(f"Сумма цифр в числе: {SumOfDigit(int(num))}")
    else:
        print("Число не трёхзначное. Ввдедите правильное число.")

def SumOfDigit(num):
    sum = 0
    while num != 0:
        sum += num%10
        num //= 10
    return sum

# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

def TaskFour():
    countCrane = int(input("Введите количество журавликов: "))
    if countCrane < 0:
        countCrane *= -1
    if countCrane % 6:
        print("Задача не имеет целочисленного решения при данном количестве журавликов.")
    else:
        print(f"Петя: {countCrane//6}\nКатя: {countCrane//6*4}\nСережа: {countCrane//6}")

# SwitchTask()
TaskFour()