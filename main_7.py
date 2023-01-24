import function_7 as fn

menuitems = [
        ("1", "Вывод автобусов"),
        ("2", "Добавление автобуса"),
        ("3", "Вывод водителей"),
        ("4", "Добавление водителя"),
        ("5", "Вывод маршрута"),
        ("6", "Добавление маршрута"),
        ("7", "Выход")
        ]

for i in menuitems:
    print(i[0], i[1])

text = int(input('>: '))

if text == 1:
    fn.print_bus()
elif text == 2:
    fn.add_bus()
elif text == 3:
    fn.print_driver()
elif text == 4:
    fn.add_driver()
elif text == 5:
    fn.print_route()
elif text == 6:
    fn.add_route()