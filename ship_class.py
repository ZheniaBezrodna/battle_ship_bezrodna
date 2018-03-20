from string import ascii_uppercase


class Game:
    def __init__(self):
        # first_field = field_generate()
        # second_fields = field_generate()
        # self.fields = [first_field, second_fields]
        self.players = [
            Player(input("Player 1: ")),
            Player(input("Player 2: "))
        ]
        self.fields = [
           Field("field.txt"),
           Field("field_2.txt")
        ]
        self.current_player = 1

    def shoot_at(self):
        self.players[0] = input("Player 1, enter move: ")

    def field_with_ships(self):
        pass

    def field_without_ships(self):
        pass


class Field:
    def __init__(self, ships, path):
        self.ships = ships
        self.field = []
        self.read_field(path)

    def read_field(self, path):
        # Reads the field from the file.
        with open(path, 'r') as file:
            for item in file.readlines():
                self.field.append(list(item.strip()))
        # print(field)
        return self.field

    def shoot_at(self):
        pass

    def field_with_ships(self):
        # Returns a list with all the coordinates of all ships.
        lst = []
        letters = ascii_uppercase
        # count = 0
        for items in range(10):
            for el in range(10):
                a = self.field[items][el]
                if a != '0':
                    lst.append((letters[items], el + 1))
                else:
                    continue
        return lst

    def field_without_ships(self):
        pass


class Player:
    def __init__(self, name):
        self._name = name
        # self._field = Field(ships)
        self.hits = 0


class Ship:
    def __init__(self, length):
        self.bow = None
        self.horizontal = None
        self.length = length
        self._hit = length * [False]

    def shoot(self):
        for items in self._hit:
            if not self._hit[items]:
                return False
        return True

