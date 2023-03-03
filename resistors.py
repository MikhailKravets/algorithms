

class Resistor:
    _COLOR_MAP = {
        "BLACK": 0,
        "BROWN": 1,
        "RED": 2,
        "ORANGE": 3,
        "YELLOW": 4,
        "GREEN": 5,
        "BLUE": 6,
        "PURPLE": 7,
        "GRAY": 8,
        "WHITE": 9
    }

    def __init__(self, colors: list[str]):
        self.colors = colors

    def resist(self):
        return self.first_band * 10 + self.second_band

    @property
    def first_band(self):
        return self._COLOR_MAP[self.colors[0]]

    @property
    def second_band(self):
        return self._COLOR_MAP[self.colors[1]]


if __name__ == '__main__':
    r = Resistor(["RED", "BLUE"])

    print(r.resist())
    print(r.first_band)
    print(r.second_band)
