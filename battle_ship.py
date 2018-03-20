from string import ascii_uppercase


def read_field(path):
    # Reads the field from the file.
    field = []
    with open(path, 'r') as file:
        for item in file.readlines():
            field.append(list(item.strip()))
    # print(field)
    return field


def has_ship(field, coordinate):
    # Сhecks whether the ship at the specified coordinates exists on the field.
    letters = ascii_uppercase
    if field[coordinate[1]-1][letters.index(coordinate[0])] == 'X':
        return print(True)
    return print(False)


def field_with_ships(field):
    # Returns a list with all the coordinates of all ships.
    lst = []
    letters = ascii_uppercase
    # count = 0
    for items in range(10):
        for el in range(10):
            a = field[items][el]
            if a != '0':
                lst.append((letters[items], el+1))
            else:
                continue
    return lst


# def ship_size(lst):
#     # Returns the ship size to the specified point.
#     letters = ascii_uppercase
#     ship_length = 1
#     lst_new = []
#     for items in lst:
#         for number in range(10):
#             for i in range(1, 4):
#                 if(letters[letters.index(items[0])+i], items[1])in lst:
#                     lst_new[number].append([letters[letters.index(items[0])+i], items[1]])
#                     # lst.remove(letters[letters.index(items[0])+i], items[1])
#                 else:
#                     break
#             for i in range(1, 4):
#                 if(letters[letters.index(items[0])-i], items[1])in lst:
#                     lst_new[number].append([letters[letters.index(items[0])+i], items[1]])
#                     # lst.remove(letters[letters.index(items[0])-i], items[1])
#                 else:
#                     break
#             for i in range(1, 4):
#                 if(items[0], items[1] + i)in lst:
#                     lst_new[number].append([items[0], items[1] + i])
#                     # lst.remove(items[0], items[1] + i)
#                 else:
#                     break
#             for i in range(1, 4):
#                 if(items[0], items[1] - i)in lst:
#                     lst_new[number].append([items[0], items[1] - i])
#                     # lst.remove(items[0], items[1] - i)
#                 else:
#                     break
#     return print(lst_new)


def field_to_str(field):
    # Writes the field to the appropriate format and displays it.
    display = ""
    for elements in field:
        display += ' '.join(elements) + '\n'
    return print(display)


result = read_field("field_2.txt")
result2 = field_with_ships(result)
print(result2)
# print(ship_size(result2))
# print(result2)
# field_with_ships(result)
