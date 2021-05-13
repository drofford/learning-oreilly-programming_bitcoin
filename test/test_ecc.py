from model.ecc import FieldElement

def test_basic():
    fe2 = FieldElement(2, 5)
    assert fe2.num == 2
    assert fe2.prime == 5
    assert repr(fe2) == "FieldElement_2(5)"

def test_zero_prime():
    try:
        a = FieldElement(3, 0)
        assert False
    except ValueError as e:
        assert str(e) == "Prime 0 must be greater than 0"
    
def test_num_bigger_than_prime():
    try:
        a = FieldElement(35, 5)
        assert False
    except ValueError as e:
        assert str(e) == "Num 35 not in field range 0 to 4"
    
def test_many():
    fe0 = FieldElement(0, 5)
    fe1 = FieldElement(1, 5)
    fe2 = FieldElement(2, 5)
    fe3 = FieldElement(3, 5)
    fe4 = FieldElement(4, 5)

    assert fe0 == fe0
    assert fe0 != fe1
    assert fe0 != fe2
    assert fe0 != fe3
    assert fe0 != fe3

def test_add():
    a = FieldElement(2, 5)
    b = FieldElement(1, 5)
    c = FieldElement(3, 5)
    assert c == a + b

    assert FieldElement(0, 5) == FieldElement(2, 5) + FieldElement(3, 5)
    
