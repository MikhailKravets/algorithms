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
    assert score == 80


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


def test_straight_flush_five_cards():
    cards = [
        Card(name="7", suit=Suits.DIAMOND.name, value=7),
        Card(name="8", suit=Suits.DIAMOND.name, value=8),
        Card(name="9", suit=Suits.DIAMOND.name, value=9),

        Card(name="10", suit=Suits.DIAMOND.name, value=10),
        Card(name="J", suit=Suits.DIAMOND.name, value=11),
    ]
    score = Combination.straight_flush(cards)
    assert score == 90


def test_straight_flush_seven_cards_small_beginning():
    cards = [
        Card(name="2", suit=Suits.DIAMOND.name, value=2),
        Card(name="7", suit=Suits.DIAMOND.name, value=7),
        Card(name="8", suit=Suits.DIAMOND.name, value=8),
        Card(name="9", suit=Suits.DIAMOND.name, value=9),

        Card(name="10", suit=Suits.DIAMOND.name, value=10),
        Card(name="J", suit=Suits.DIAMOND.name, value=11),
    ]
    score = Combination.straight_flush(cards)
    assert score == 90


def test_straight_flush_seven_cards_high_end():
    cards = [
        Card(name="6", suit=Suits.DIAMOND.name, value=6),
        Card(name="7", suit=Suits.DIAMOND.name, value=7),
        Card(name="8", suit=Suits.DIAMOND.name, value=8),
        Card(name="K", suit=Suits.DIAMOND.name, value=13),

        Card(name="9", suit=Suits.DIAMOND.name, value=9),
        Card(name="10", suit=Suits.DIAMOND.name, value=10),
    ]
    score = Combination.straight_flush(cards)
    assert score == 90

# TODO: finish tests for straight flush


def test_full_house():
    cards = [
        Card(name="10", suit=Suits.DIAMOND.name, value=6),
        Card(name="K", suit=Suits.HEART.name, value=7),
        Card(name="K", suit=Suits.DIAMOND.name, value=8),
        Card(name="K", suit=Suits.SPADES.name, value=13),

        Card(name="9", suit=Suits.DIAMOND.name, value=9),
        Card(name="10", suit=Suits.DIAMOND.name, value=10),
    ]
    score = Combination.full_house(cards)
    assert score == 70


def test_full_house_no_combination():
    cards = [
        Card(name="10", suit=Suits.DIAMOND.name, value=6),
        Card(name="K", suit=Suits.HEART.name, value=7),
        Card(name="K", suit=Suits.DIAMOND.name, value=8),
        Card(name="A", suit=Suits.SPADES.name, value=13),

        Card(name="9", suit=Suits.DIAMOND.name, value=9),
        Card(name="10", suit=Suits.DIAMOND.name, value=10),
    ]
    score = Combination.full_house(cards)
    assert score == 0


def test_flush():
    cards = [
        Card(name="10", suit=Suits.DIAMOND.name, value=6),
        Card(name="K", suit=Suits.HEART.name, value=7),
        Card(name="K", suit=Suits.DIAMOND.name, value=8),
        Card(name="A", suit=Suits.SPADES.name, value=13),

        Card(name="9", suit=Suits.DIAMOND.name, value=9),
        Card(name="10", suit=Suits.DIAMOND.name, value=10),
    ]
    score = Combination.flush(cards)
    assert score == 60


def test_flush_no_combination():
    cards = [
        Card(name="10", suit=Suits.DIAMOND.name, value=6),
        Card(name="K", suit=Suits.HEART.name, value=7),
        Card(name="K", suit=Suits.DIAMOND.name, value=8),
        Card(name="A", suit=Suits.SPADES.name, value=13),

        Card(name="9", suit=Suits.DIAMOND.name, value=9),
        Card(name="10", suit=Suits.HEART.name, value=10),
    ]
    score = Combination.flush(cards)
    assert score == 0


def test_straight():
    cards = [
        Card(name="7", suit=Suits.SPADES.name, value=7),
        Card(name="8", suit=Suits.HEART.name, value=8),
        Card(name="9", suit=Suits.DIAMOND.name, value=9),

        Card(name="10", suit=Suits.DIAMOND.name, value=10),
        Card(name="J", suit=Suits.DIAMOND.name, value=11),
    ]
    score = Combination.straight(cards)
    assert score == 50


def test_straight_no_combination():
    cards = [
        Card(name="6", suit=Suits.SPADES.name, value=6),
        Card(name="8", suit=Suits.HEART.name, value=8),
        Card(name="9", suit=Suits.DIAMOND.name, value=9),

        Card(name="10", suit=Suits.DIAMOND.name, value=10),
        Card(name="J", suit=Suits.DIAMOND.name, value=11),
    ]
    score = Combination.straight(cards)
    assert score == 0
