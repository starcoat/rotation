Coordinates = tuple[int, int]


class Stick:

    def __init__(self, symbol: str, coords: list[Coordinates]) -> None:
        self.symbol = symbol
        self.coords = coords


class Playground:

    def __init__(self, size: int, door: Coordinates) -> None:
        self.size = size
        self.door = door

    def __str__(self) -> str:
        pass

    def add_stick(self, stick: Stick) -> None:
        pass