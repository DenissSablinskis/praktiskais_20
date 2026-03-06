
from app import izvilkt_kvadratsakni, saskaitit


def test_izvilkt_kvadratsakni_25():
    assert izvilkt_kvadratsakni(25) == 5

def test_izvilkt_kvadratsakni_36():
    assert izvilkt_kvadratsakni(36) == 6

def test_izvilkt_kvadratsakni_49():
    assert izvilkt_kvadratsakni(49) == 7

def test_saskaitit():
    assert saskaitit(5, 5) == 10

def test_saskaitit():
    assert saskaitit(10, 5) == 15

def test_saskaitit():
    assert saskaitit(3, 9) == 12

