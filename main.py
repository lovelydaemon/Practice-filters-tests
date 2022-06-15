# Написать функцию фильтрации объявлений по диапазону заданных цен
items = [
        {
            'title': '3-к. квартира, 80м2, 13/22 эт.',
            'rooms': 3,
            'price': 70000,
            'petFriendly': True
        },
        {
            'title': '2-к. квартира, 45м2, 5/5 эт.',
            'rooms': 2,
            'price': 60000,
            'petFriendly': False,
            'deposit': 60000
        },
        {
            'title': '2-к. квартира, 44,4м2, 4/4 эт.',
            'rooms': 2,
            'price': 45000,
            'petFriendly': True,
            'agency': True
        },
        {
            'title': '2-к. квартира, 44,4м2, 5/5 эт.',
            'rooms': 2,
            'price': 45000,
            'petFriendly': True,
            'agency': True,
            'fee': 45000
        },
        {
            'title': '1-к. квартира, 20м2, 2/5 эт.',
            'rooms': 1,
            'petFriendly': True,
            'agency': True,
        },
]



def sort_ads_by_price(data:list, min_price:int=0, max_price:int|None=None) -> list:
    """Сортировка объявлений по цене"""
    if not isinstance(min_price, int) or not isinstance(max_price, int|None):
        raise TypeError('Цена должна быть введена в виде числа')
    if min_price < 0:
        raise ValueError('Мин. цена должна быть больше нуля')
    if max_price:
        if max_price < 0:
            raise ValueError('Макс. цена должна быть больше нуля')
        if max_price < min_price:
            raise ValueError('Макс. цена должна быть больше мин. цены')

    if not max_price:
        return [item for item in data if item.get('price') and item.get('price') >= min_price]
    return [item for item in data if item.get('price') and min_price <= item.get('price') <= max_price]


def sort_ads_by_title(data:list, title:str|None=None) -> list:
    """Сортировка объявлений по тексту"""
    if not isinstance(title, str|None):
        raise TypeError('В поле текста подается строка')

    if not title: return data
    return [item for item in data if title in item.get('title')]


if __name__ == '__main__':
    results = sort_ads_by_price(items, max_price=45000)
    print(results)
