import pytest

from src.item import Item


@pytest.fixture
def test_item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def test_item2():
    return Item("Ноутбук", 20000, 5)
