from collections import Counter

from black_jack import Deck


def test_deck_creation():
    deck = Deck()

    assert len(deck) == 52

    names = [v.name for v in deck.cards]
    counter = Counter(names)

    for v in counter.values():
        assert v == 4
