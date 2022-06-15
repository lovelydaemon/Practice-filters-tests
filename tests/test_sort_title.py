from main import sort_ads_by_title
import pytest


items = [{
            'title': '2-к. квартира, 44,4м2, 5/5 эт.',
            'rooms': 2,
            'price': 45000,
            'petFriendly': True,
            'agency': True,
            'fee': 45000
        }]

def test_title_default():
    """Без уточнения описания"""
    assert sort_ads_by_title(items, title=None) == items

def test_title_bad_type():
    """В описании неправильный тип данных"""
    with pytest.raises(TypeError):
        sort_ads_by_title(items, title=12)

def test_title_not_exists():
    """Нет совпадений с описанием"""
    assert sort_ads_by_title(items, title='45') == []

def test_title_exists():
    """Есть совпадение с описанием"""
    assert sort_ads_by_title(items, title='кварти') == items
