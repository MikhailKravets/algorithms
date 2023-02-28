from cards.deck import Card, Deck

PLAYER = 3

"""
1. 3 players
2. Dealer moving right each round
3. Small blind and big blind right to the dealer
4. Amount of $ for each player. We cannot add $ during the game

5. Combinations
6. Player can fold
"""

"""
Jd 7h 8h 2c 9s

P1: 7c As
P2: 7s Kd
"""


class Player:

    def __init__(self, name: str, initial_bank: int):
        self.name = name
        self.bank: int = initial_bank
        self.hand: tuple[Card, Card]

        self.is_dealer = False

    def check(self):
        pass

    def fold(self):
        pass

    def call(self):
        pass

    def raise_(self):
        pass

    def __str__(self):
        return f"Player {self.name}. Bank {self.bank}"


class Table:

    def __init__(self, player: list[Player], small_blind: int = 2):
        self.deck = Deck()
        self.players = player

        self.bank = 0
        self.cards: list[Card]  # Cards on table
        self.small_blind_sum = small_blind
        self.big_bling_sum = small_blind * 2

        self.new_round()
        self._current_dealer_idx = 0

    @property
    def dealer(self) -> Player:
        return self.players[self._current_dealer_idx]

    @property
    def small_blind(self) -> Player:
        return self.players[self._current_dealer_idx + 1]

    @property
    def big_blind(self) -> Player:
        return self.players[self._current_dealer_idx + 2]

    def new_round(self):
        assert self.bank == 0, "Bank must be 0 before new round"
        self.deck = Deck()


class Combination:

    def __init__(self, cards: list[Card]):  # 7 cards. 5 from table and 2 from player
        # TODO: implement a case when you can pass less than 7 cards.
        #       A case when we calculate combinations in the mid-game
        self.score = 0


if __name__ == '__main__':
    p1 = Player("Bob", 100)
    p2 = Player("Jon Snow", 100)
    p3 = Player("Kirill", 100)

    table = Table([p1, p2, p3], small_blind=2)  # 2 / 4
