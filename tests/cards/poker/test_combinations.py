from cards.deck import Card, Suits
from cards.poker import Combination


def test_royal_flush():
    cards = [
        Card(name="10", suit=Suits.HEART.name, value=7),
        Card(name="J", suit=Suits.HEART.name, value=7),
        Card(name="Q", suit=Suits.HEART.name, value=7),
        Card(name="7", suit=Suits.SPADES.name, value=10),
        Card(name="9", suit=Suits.CROSS.name, value=10),

        Card(name="K", suit=Suits.HEART.name, value=7),
        Card(name="A", suit=Suits.HEART.name, value=10),
    ]
    score = Combination.royal_flush(cards)
    assert score == 100


def test_four_of_a_kind():
    cards = [
        Card(name="7", suit=Suits.HEART.name, value=7),
        Card(name="7", suit=Suits.DIAMOND.name, value=7),
        Card(name="7", suit=Suits.CROSS.name, value=7),

        Card(name="7", suit=Suits.SPADES.name, value=7),
        Card(name="J", suit=Suits.DIAMOND.name, value=10),
    ]
    score = Combination.four_of_a_kind(cards)
    assert score == 40


def test_four_of_a_kind_not_in_cards():
    cards = [
        Card(name="7", suit=Suits.HEART.name, value=7),
        Card(name="7", suit=Suits.DIAMOND.name, value=7),
        Card(name="7", suit=Suits.CROSS.name, value=7),

        Card(name="8", suit=Suits.SPADES.name, value=7),
        Card(name="J", suit=Suits.DIAMOND.name, value=10),
    ]
    score = Combination.four_of_a_kind(cards)
    assert score == 0
