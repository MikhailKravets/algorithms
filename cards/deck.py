import dataclasses
import enum
import random


@dataclasses.dataclass
class Card:
    name: str
    suit: str
    value: int
    is_special: bool = False

    @property
    def special_value(self):
        return 1


class Suits(enum.Enum):
    DIAMOND = "Diamond"
    HEART = "Heart"
    CROSS = "Cross"
    SPADES = "Spades"


class Deck:
    _VALUES = [
        ("2", 2, False),
        ("3", 3, False),
        ("4", 4, False),
        ("5", 5, False),
        ("6", 6, False),
        ("7", 7, False),
        ("8", 8, False),
        ("9", 9, False),
        ("10", 10, False),
        ("J", 10, False),
        ("Q", 10, False),
        ("K", 10, False),
        ("A", 11, True),
    ]

    def __init__(self):
        self.cards = []

        for name, value, is_special in self._VALUES:
            for suit in Suits:
                card = Card(name=name, value=value, suit=suit, is_special=is_special)
                self.cards.append(card)

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)
