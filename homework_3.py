import random

def SwitchTask():
    taskNum = int(input("Введите номер задачи из домашней работы: "))
    while taskNum != 0:
        if taskNum == 16:
            Task16()
        elif taskNum == 18:
            Task18()
        elif taskNum == 20:
            Task20()
        else:
            print("Задачи с таким номером не задавали. Введите правильный номер задачи.")
        taskNum = int(input("Если все проведено, введите 0.\nВведите номер задачи из домашней работы: "))

# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2

def Task16():
    size = int(input("Введите размер массива: "))
    while size != 0:
        num = int(input("Введите искомое число: "))
        intArray = []
        count = 0
        for i in range(size):
            intArray.append(random.randint(1, int(size/2)))
            if num == intArray[i]:
                count += 1
        print(intArray)
        print(count)
        size = int(input("Чтобы продолжить, введите размер нового массива.\nДля остановки введите 0. "))

# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

def Task18():
    size = int(input("Введите размер массива: "))
    while size != 0:
        intArray = []
        for i in range(size):
            intArray.append(random.randint(1, 10))
        print(intArray)
        num = int(input("Введите число, к которому нужно найти ближайшее: "))
        intDiff = []
        minDiff = 0
        flag = True
        for i in range(len(intArray)):
            intDiff.append(abs(num - intArray[i]))
            if intDiff[i] != 0 and flag:
                minDiff = i
                flag = False
        print(intDiff)
        for i in range(minDiff + 1, len(intDiff)):
            if intDiff[i] != 0:
                if intDiff[i] < intDiff[minDiff]:
                    minDiff = i
                elif intDiff[minDiff] == intDiff[i]:
                    if intArray[i] < num:
                        minDiff = i
        print(intArray[minDiff])
        size = int(input("Чтобы продолжить, введите размер нового массива.\nДля остановки введите 0. "))

# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# Ввод: ноутбук
# Вывод: 12

def Task20():
    dictionEN = {
        "AEIOULNSTR": 1,
        "DG": 2,
        "BCMP": 3,
        "FHVWY": 4,
        "K": 5,
        "JX": 8,
        "QZ": 10
    }
    dictionRU = {
        "АВЕИНОРСТ": 1,
        "ДКЛМПУ": 2,
        "БГЁЬЯ": 3,
        "ЙЫ": 4,
        "ЖЗХЦЧ": 5,
        "ШЭЮ": 8,
        "ФЩЪ": 10
    }
    word = str(input("Введите слово. Поле не должно быть пустым.\n"))
    while word != "":
        sum = 0
        ru = False
        en = False
        for i in word:
            for key in dictionRU:
                if i.upper() in key:
                    sum += dictionRU[key]
                    ru = True
            for key in dictionEN:
                if i.upper() in key:
                    sum += dictionEN[key]
                    en = True
            if ru and en:
                print("Слово должно состоять из букв одного языка.")
                break
        if not (ru and en):
            print(sum)
        word = str(input("Введите новое слово. Чтобы закончить, оставьте поле пустым.\n"))

SwitchTask()