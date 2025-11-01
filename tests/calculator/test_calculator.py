from src.calculator.calculator import Calculator

def test_addition():
    c = Calculator()
    assert c.add(1,2) == 3
    assert c.add("one","four") == 5
    assert c.add("III","IV") == 7

def test_factorize():
    c = Calculator()
    assert c.factorize(12) == [2,2,3]
