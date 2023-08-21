import pytest


def test_language(test_keyboard1):
    assert str(test_keyboard1.language) == "EN"


def test_change_lang(test_keyboard1):
    test_keyboard1.change_lang()
    assert str(test_keyboard1.language) == "RU"
    test_keyboard1.change_lang()
    assert str(test_keyboard1.language) == "EN"
