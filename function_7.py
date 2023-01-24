def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(', '))
    return result


def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write('\n' + data_list)

def show(data):
    str_data = ''
    for item in data:
        str_data += item[0]
        for i in range(1, len(item)):
            str_data += ', ' + item[i]
        str_data += '\n'
    print(str_data)

def list_to_str(data):
    return ",".join(data) + '\n'

def print_bus():
    buses = read_data_from_file('bus_7.txt')
    show(buses)
    value = input('Хотите увидеть дополнительную информацию? Y/N>:')
    if value == 'Y':
        routes = read_data_from_file('marsh_7.txt')
        drivers = read_data_from_file('driver_7.txt')
        for bus, bus_num in buses:
            route, driver = item_by_id_2(bus, routes)
            driver_name = item_by_id(driver, drivers)
            print('{}, {}, {}, {}'.format(bus,bus_num,route,driver_name))
        input()

def add_bus():
    save_data_to_file('bus_7.txt', input('>:'))

def print_driver():
    drivers = read_data_from_file('driver_7.txt')
    show(drivers)
    value = input('Хотите увидеть дополнительную информацию? Y/N>:')
    if value == 'Y':
        routes = read_data_from_file('marsh_7.txt')
        buses = read_data_from_file('bus_7.txt')
        for driver, driver_name in drivers:
            route, bus = item_by_id_3(driver, routes)
            bus_num = item_by_id(bus, buses)
            print('{}, {}, {}, {}'.format(driver,driver_name,route,bus_num))
        input()

def add_driver():
    save_data_to_file('driver_7.txt', input('>:'))

def print_route():
    routes = read_data_from_file('marsh_7.txt')
    show(routes)
    value = input('Хотите увидеть дополнительную информацию? Y/N>:')
    if value == 'Y':
        drivers = read_data_from_file('driver_7.txt')
        buses = read_data_from_file('bus_7.txt')
        for name, number, bus, driver in routes:
            bus_num = item_by_id(bus, buses)
            driver_name = item_by_id(driver, drivers)
            print('{}, {}, {}, {}, {}, {}'.format(name,number,driver,driver_name,bus,bus_num))
        input()

def add_route():
    save_data_to_file('marsh_7.txt', input('>:'))

def item_by_id(id, records):
    for id_rec, item in records:
        if id == id_rec:
            return item
    return id
        
def item_by_id_2(id, records):
    for id_rec, item, item1, item2 in records:
        if id == item1:
            return id_rec, item2
    return '-', '-'

def item_by_id_3(id, records):
    for id_rec, item, item1, item2 in records:
        if id == item2:
            return id_rec, item1
    return '-', '-'