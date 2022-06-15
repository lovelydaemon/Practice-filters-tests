from filters import sort_ads_by_price
import pytest


items_with_price = [
        {
            'title': '3-к. квартира, 80м2, 13/22 эт.',
            'rooms': 3,
            'price': 70000,
            'petFriendly': True
        }]

items_without_price = [
        {
            'title': '1-к. квартира, 20м2, 2/5 эт.',
            'rooms': 1,
            'petFriendly': True,
            'agency': True,
        }]

class TestPriceNormalMode:
    def test_price_default(self):
        """Без уточнения диапазона"""
        assert sort_ads_by_price(items_with_price) == items_with_price

    def test_price_min(self):
        """Указана минимальная цена"""
        assert sort_ads_by_price(items_with_price, min_price=65000) == items_with_price

    def test_price_max(self):
        """Указана максимальная цена"""
        assert sort_ads_by_price(items_with_price, max_price=80000) == items_with_price

    def test_price_min_max(self):
        """Указана мин и макс цена"""
        assert sort_ads_by_price(items_with_price, min_price=45000, max_price=83000) == items_with_price

    def test_price_min_morethan_price(self):
        """Мин цена больше, чем цена объявлений"""
        assert sort_ads_by_price(items_with_price, min_price=72000) == []

    def test_price_max_lessthan_price(self):
        """Макс цена меньше, чем цена объявлений"""
        assert sort_ads_by_price(items_with_price, max_price=60000) == []

    def test_price_not_exists(self):
        """Цена не указана в объявлениях"""
        assert sort_ads_by_price(items_without_price, max_price=80000) == []


class TestPriceRaises:
    def test_price_min_wrong_type(self):
        """Мин цена неправильный тип данных"""
        with pytest.raises(TypeError):
            sort_ads_by_price(items_with_price, min_price='13900')

    def test_price_max_wrong_type(self):
        """Макс цена неправильный тип данных"""
        with pytest.raises(TypeError):
            sort_ads_by_price(items_with_price, max_price='79999')

    def test_price_min_negative(self):
        """Мин цена отрицательная"""
        with pytest.raises(ValueError):
            sort_ads_by_price(items_with_price, min_price=-10000)

    def test_price_max_negative(self):
        """Макс цена отрицательная"""
        with pytest.raises(ValueError):
            sort_ads_by_price(items_with_price, max_price=-90000)

    def test_price_min_morethan_max(self):
        """Мин цена больше, чем макс цена"""
        with pytest.raises(ValueError):
            sort_ads_by_price(items_with_price, min_price=50000, max_price=30000)
