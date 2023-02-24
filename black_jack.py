import enum
import dataclasses
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


class Player:

    def __init__(self):
        self.cards = []
        self.score = 0

    def add(self, card: Card):
        self.cards.append(card)
        value = card.value

        if card.is_special:
            if self.score + card.value > 21:
                value = card.special_value

        if self.score + value > 21:
            raise ValueError("You exceeded max score 21. You lose")

        self.score += value


class BlackJack:

    def __init__(self):
        self.deck = self.reset()

    def step(self):
        return self.deck.cards.pop(0)

    def reset(self):
        self.deck = Deck()
        return self.deck


class Simulation:

    def __init__(self, players: int = 2):
        self.black_jack = BlackJack()
        self.players = [Player() for _ in range(players)]

    def round(self):
        for v in self.players:
            while True:
                card = self.black_jack.step()
                try:
                    v.add(card)
                except ValueError:
                    print(f"Round is end for player {v}")
                    break
                print(f"Player {v}. Card: {card.name}-{card.suit.value}. Score {v.score}")
            print("")

    def reset(self):
        self.black_jack.reset()
        self.players = [Player() for _ in self.players]


if __name__ == '__main__':
    # TODO: make normal blackjack game
    # TODO: cover functional with tests
    s = Simulation()
    s.round()

