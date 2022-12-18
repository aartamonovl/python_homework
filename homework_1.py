

def SwitchTask ():
    taskNum = int(input("Введите номер задачи из домашней работы: "))
    taskNumber = {
        2: TaskTwo(),
        # taskNum == 4: TaskFour(),
        # taskNum == 6: TaskSix(),
        # taskNum == 8: TaskEight()
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

# SwitchTask()
TaskTwo ()