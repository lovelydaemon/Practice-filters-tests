

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
