import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def test_item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def test_item2():
    return Item("Ноутбук", 20000, 5)


@pytest.fixture
def test_phone1():
    return Phone("iPhone 14", 120_000, 5, 2)
