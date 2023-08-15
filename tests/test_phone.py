import pytest


def test_repr(test_phone1):
    assert repr(test_phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(test_phone1):
    assert str(test_phone1) == 'iPhone 14'


def test_number_of_sim(test_phone1):
    assert test_phone1.number_of_sim == 2
    test_phone1.number_of_sim = 1
    assert test_phone1.number_of_sim == 2
    test_phone1.number_of_sim = 2.5
    assert test_phone1.number_of_sim == 2
    with pytest.raises(Exception):
        test_phone1.number_of_sim = -1
