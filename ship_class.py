

class Game:
    def __init__(self):
        # first_field = field_generate()
        # second_fields = field_generate()
        # self.fields = [first_field, second_fields]
        first_name = Player(input("Player 1: "))
        second_name = Player(input("Player 2: "))
        self.players = [first_name, second_name]
        self.current_player = 1

    def shoot_at(self):
        self.players[0] = input("Player 1, enter move: ")

    def field_with_ships(self):
        pass

    def field_without_ships(self):
        pass


class Field:
    def __init__(self, ships):
        self.ships = ships

    def shoot_at(self):
        pass

    def field_with_ships(self):
        pass

    def field_without_ships(self):
        pass


class Player:
    def __init__(self, name):
        self._name = name
        self._field = Field(ships)
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

