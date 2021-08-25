Coordinates = tuple[int, int]


class Stick:

    def __init__(self, symbol: str, coords: list[Coordinates]) -> None:
        self.symbol = symbol
        self.coords = coords


class Playground:

    def __init__(self, size: int, door: Coordinates) -> None:
        self.size = size
        self.door = door
        self.rotation = 0
        self.sticks = []

        # Leinwand initialisieren
        self.canvas = [[' ' for x in range(size)] for y in range(size)]
        for s in range(size):
            self.canvas[s][0] = self.canvas[0][s] = self.canvas[s][size - 1] = self.canvas[size - 1][s] = '#'
        self.canvas[door[0]][door[1]] = ' '

    def __str__(self) -> str:
        result = ''
        for x in range(len(self.canvas)):
            for y in range(len(self.canvas[x])):
                result += self.canvas[x][y]
            result += '\n'
        return result

    def add_stick(self, stick: Stick) -> None:
        self.sticks.append(stick)
        for c in stick.coords:
            self.canvas[c[0]][c[1]] = stick.symbol