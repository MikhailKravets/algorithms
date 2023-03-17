import collections

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
        self.hand: list[Card, Card] | None = None

        self.is_dealer = False

    def check(self):
        pass

    def fold(self):
        pass

    def call(self):
        pass

    def raise_(self):
        pass

    def set_hand(self, cards):
        self.hand = cards

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

        # TODO: think how to increment the value!
        self._current_player_idx = (self._current_dealer_idx + 3) % len(self.players)

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

    def get_cards(self, amount: int = 1) -> list[Card]:
        return [self.deck.pop() for _ in range(amount)]


class Combination:

    def __init__(self):  # 7 cards. 5 from table and 2 from player
        pass

    @staticmethod
    def score(cards: list[Card]):
        # TODO: 1. Go through highest to lowest combinations
        #   2. Each combination should return score
        #   3. Return score
        if score := Combination.royal_flush(cards) != 0:
            return score
        if score := Combination.straight_flush(cards) != 0:
            return score
        if score := Combination.four_of_a_kind(cards) != 0:
            return score

    @staticmethod
    def royal_flush(cards: list[Card]) -> int:
        # 10 J Q K A  - the same suit
        tmp = ("10", "J", "Q", "K", "A")

        if len(cards) < len(tmp):
            return 0

        c_name = [v.name for v in cards]
        c_full = []
        for v in tmp:
            if v in c_name:
                idx = c_name.index(v)
                c_full.append(cards[idx])

        c = collections.Counter([v.suit for v in c_full])

        if len(c) == 1:
            return 100

        return 0

    @staticmethod
    def straight_flush(cards: list[Card]) -> int:   # 4D 5D 6D 8C 10D    7D 8D
        c = collections.Counter([v.suit for v in cards])

        flush_suit = None
        for suit, count in c.items():
            if count >= 5:
                flush_suit = suit

        if not flush_suit:
            return 0

        # TODO: 4D 5D 6D 7D 8D 10D

        # 4 5 6 7 8 10
        ranks = sorted([v.value for v in cards if v.suit == flush_suit])

        stride = 1
        sequence = 1
        for i in range(len(ranks) - 1):
            if sequence >= 4:
                return 90

            if ranks[i + 1] - ranks[i] == stride:
                sequence += 1
            else:
                sequence = 1
        return 0

    @staticmethod
    def four_of_a_kind(cards: list[Card]) -> int:
        counter = collections.Counter([v.name for v in cards])
        for v in counter.values():
            if v == 4:
                return 80
        return 0

    @staticmethod
    def full_house(cards: list[Card]) -> int:   # KD KH KS 8C 10D    7D 8D
        counter = collections.Counter([v.name for v in cards])
        values = counter.values()

        # TODO: players may have different full house combinations.
        #   We must ensure that the user with the highest full house
        #   combination wins the game.
        #   So, we should also check the value of the card itself.

        if 3 in values and 2 in values:
            return 70
        return 0

    @staticmethod
    def flush(cards: list[Card]) -> int:   # KD 2D 5D 8C 8H    7S 8D
        counter = collections.Counter([v.suit for v in cards])
        values = counter.values()

        if any(v >= 4 for v in values):
            return 60
        return 0

    @staticmethod
    def straight(cards: list[Card]) -> int:   # 4D 5S 6H 8C 10D    7D 8D
        ranks = sorted([v.value for v in cards])

        stride = 1
        sequence = 1
        for i in range(len(ranks) - 1):
            if sequence >= 4:
                return 50

            if ranks[i + 1] - ranks[i] == stride:
                sequence += 1
            else:
                sequence = 1
        return 0

    @staticmethod
    def three_of_a_kind(cards: list[Card]) -> int:   # 4D 8S 6H 8C 10D    7D 8D
        counter = collections.Counter([v.name for v in cards])
        v = counter.values()
        if 3 in v:
            return 40
        return 0

    @staticmethod
    def two_pair(cards: list[Card]) -> int:   # 4D 7S 6H 8C 10D    7D 8D
        counter = collections.Counter([v.name for v in cards])

        i = 0
        for v in counter.values():
            if v == 2:
                i += 1
            if i == 2:
                return 30
        return 0

    @staticmethod
    def pair(cards: list[Card]) -> int:  # 4D 2S 6H 8C 10D    7D 8D
        counter = collections.Counter([v.name for v in cards])
        if 2 in counter.values():
            return 20
        return 0

    @staticmethod
    def high_card(cards: list[Card]) -> int:
        return max([v.value for v in cards])


if __name__ == '__main__':
    p1 = Player("Bob", 100)
    p2 = Player("Jon Snow", 100)
    p3 = Player("Kirill", 100)

    table = Table([p1, p2, p3], small_blind=2)  # 2 / 4

    p1.set_hand(table.get_cards(2))
    p2.set_hand(table.get_cards(2))
    p3.set_hand(table.get_cards(2))
