from string import ascii_uppercase


def read_field(path):
    field = []
    with open(path, 'r') as file:
        for item in file.readlines():
            field.append(list(item.strip()))
    print(field)
    return field


def has_ship(field, coordinate):
    letters = ascii_uppercase
    if field[coordinate[1]-1][letters.index(coordinate[0])] == 'X':
        return print(True)
    return print(False)


def field_with_ships(field):
    lst = []
    letters = ascii_uppercase
    # count = 0
    for items in range(10):
        for el in range(10):
            if field[items][el] == 'X':
                lst.append((letters[items], el+1))
            else:
                continue
    return lst


def ship_size(lst, coord):
    letters = ascii_uppercase
    ship_length = 1
    if coord not in lst:
        return 0
    for i in range(1, 4):
        if(letters[letters.index(coord[0])+i], coord[1])in lst:
            ship_length += 1
        else:
            break
    for i in range(1, 4):
        if(letters[letters.index(coord[0])-i], coord[1])in lst:
            ship_length += 1
        else:
            break
    for i in range(1, 4):
        if(coord[0], coord[1] + i)in lst:
            ship_length += 1
        else:
            break
    for i in range(1, 4):
        if(coord[0], coord[1] - i)in lst:
            ship_length += 1
        else:
            break
    return ship_length


def field_to_str(field):
    display = ""
    for elements in field:
        display += ' '.join(elements) + '\n'
    return print(display)


read_field("field.txt")