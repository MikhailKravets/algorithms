from cards.deck import Card, Deck


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

