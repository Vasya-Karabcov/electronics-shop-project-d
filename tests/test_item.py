import pytest

from src.item import Item


def test_calculate_total_price(test_item1, test_item2):
    assert test_item1.calculate_total_price() == 200000
    assert test_item2.calculate_total_price() == 100000


def test_apply_discount(test_item1):
    assert test_item1.apply_discount() == None
    assert test_item1.pay_rate == 1.0


def test_instantiate_from_csv(test_item1):
    test_item1.instantiate_from_csv()
    assert len(test_item1.all) == 5


def test_name(test_item1):
    assert test_item1.name == "Смартфон"
    test_item1.name = 'СуперСмартфон'
    assert test_item1.name == "Смартфон"
    test_item1.name = 'Смарт'
    assert test_item1.name == "Смарт"


@pytest.mark.parametrize('number, extented', [
    ('1', 1),
    ('2', 2)
])
def test_string_to_number(number, extented):
    assert Item.string_to_number(number) == extented


def test_repr(test_item1):
    assert repr(test_item1) == "Item('Смартфон', 10000, 20)"


def test_str(test_item1):
    assert str(test_item1) == 'Смартфон'