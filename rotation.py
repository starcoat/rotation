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

		if self.rotation == 0:
			for x in range(self.size):
				for y in range(self.size):
					result += self.canvas[x][y]
				result += '\n'
		elif self.rotation == 90:
			for x in range(self.size):
				for y in range(self.size):
					result += self.canvas[self.size - 1 - y][x]
				result += '\n'
		elif self.rotation == 180:
			for x in range(self.size):
				for y in range(self.size):
					result += self.canvas[self.size - 1 - x][self.size - 1 - y]
				result += '\n'
		elif self.rotation == 270:
			for x in range(self.size):
				for y in range(self.size):
					result += self.canvas[y][self.size - 1 - x]
				result += '\n'
		
		return result

	def add_stick(self, stick: Stick) -> None:
		self.sticks.append(stick)
		for c in stick.coords:
			self.canvas[c[0]][c[1]] = stick.symbol

	def rotate(self, direction: str) -> None:
		if direction == 'CW':
			self.rotation = (self.rotation + 90) % 360
		elif direction == 'CCW':
			self.rotation = (self.rotation + 270) % 360

	def fall_down(self) -> None:
		pass
