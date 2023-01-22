path = 'phonebook.txt'
enc = 'utf8'

def read_file(path):
    i = 1
    result = []
    with open(path, 'r', encoding=enc) as data:
        for line in data:
            line = f'{str(i)}, '  + line
            result.append(line.replace(',', '').split())
            i += 1
    return result

def show(str_res):
    print('№ строки, Фамилия, Имя, Отчество, Телефон')
    print(str_res)

def list_to_str(lst):
    result = ''
    for i in range(len(lst)):
        result += '    ' + lst[i][0] + '.    ' + lst[i][1]
        for j in range(2, len(lst[i])):
            result += ', ' + lst[i][j]
        result += '\n'
    return result

def show_all():
    record_list = read_file(path)
    str_res = list_to_str(record_list)
    show(str_res)

def find_record(inp):
    value = input_for_search(inp)
    record_list = read_file(path)
    res_search = search_in_data(record_list, value)
    str_res = list_to_str(res_search)
    show(str_res)

def input_for_search(value):
    if value == 3:
        return ['', '', '', input('Введите телефон для поиска: ')]
    else:
        return ['', input('Введите имя для поиска: '), '', '']

def search_in_data(record_list, value):
    copy_list = record_list.copy()
    res_search = []
    for i in range(len(record_list)):
        count = 0
        k = 0
        for j in range(1, len(copy_list[i])):
            if value[0][j-1]!= '':
                k +=1
                if copy_list[i][j].lower().find(value[0][j-1].lower()) != -1:
                    count += 1
        if count == k:
            res_search.append(copy_list[i])
    return res_search

def add_new_record():
    new_rec = new_record()
    str_new_rec = list_to_str_add(new_rec)
    add_to_file(path, str_new_rec)

def new_record():
    new_rec = [(input('Фамилия: '),
               input('Имя: '),
               input('Отчество: '),
               input('Телефон: ' ))]
    return new_rec

def add_to_file(path, new_rec):
    new_rec = '\n' + new_rec
    with open(path, 'a', encoding = enc) as data:
        data.write(new_rec)

def list_to_str_add(rec):
    str_rec = ''
    for i in range(len(rec)):
        if str(rec[i][0]).isdigit():
            rec[i].pop(0)
        str_rec +=  str(rec[i][0])
        for j in range(1, len(rec[i])):
            str_rec += ', ' + rec[i][j]
        str_rec += '\n'
    return str_rec

def create_filter_file(lst, del_list):
    res_list = lst.copy()
    k = 0
    for i in range(len(del_list)):
        for j in range(len(lst)):
            if int(lst[j][0]) == int(del_list[i][0]):
                res_list.pop(j-k)
                k += 1
    return res_list

def del_record():
    del_rec = new_record()
    all_data = read_file(path)
    del_record_list = search_in_data(all_data, del_rec)
    if len(del_record_list) == 0:
        print('Удалять нечего')
    else:
        new_data = create_filter_file(all_data, del_record_list)
        str_new_data = list_to_str_add(new_data)
        write_file(str_new_data[:-1])

def write_file(new_str):
    with open(path, 'w', encoding=enc) as data:
        data.write(new_str)

def change_tel_record():
    print('У какого контакта вы хотите поменять телефон?')
    value = new_record()
    record_list = read_file(path)
    res_search = search_in_data(record_list, value)
    str_res = list_to_str(res_search)
    show(str_res)
    new_tel = str(input('Введите новый номер телефона для контакта: '))
    new_list = change_tel(record_list, res_search, new_tel)
    new_list_str = list_to_str_add(new_list)
    write_file(new_list_str)

def change_tel(all_rec, rec_list, value):
    copy_list = rec_list.copy()
    for i in range(len(copy_list)):
        copy_list[i][-1] = value
        for j in range(len(all_rec)):
            if copy_list[i][0] == all_rec[j][0]:
                all_rec[j] = copy_list[i]
    return all_rec

def main():
    while True:
        print('\nВведите номер действия:\n' + 
            '1 - Показать все записи\n' +
            '2 - Найти запись по вхождению частей имени\n' +
            '3 - Найти запись по телефону\n' +
            '4 - Добавить новый контакт\n' +
            '5 - Удалить контакт\n' +
            '6 - Изменить номер телефона у контакта\n' +
            '7 - Выход\n')
        value = int(input(':'))
        match value:
            case 1:
                show_all()
            case 2:
                find_record(value)
            case 3:
                find_record(value)
            case 4:
                add_new_record()
            case 5:
                del_record()
            case 6:
                change_tel_record()
            case 7:
                break
            case _:
                print('Такого пункта в меню нет.')

main()