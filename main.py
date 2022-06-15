from filters import sort_ads_by_price, sort_ads_by_title


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


def main():
    results = sort_ads_by_price(items, max_price=45000)
    print('Объявления, отсортированные по цене')
    for ad in results:
        print(ad)

    results = sort_ads_by_title(items, title='44')
    print('Объявления, отсортированные по описанию')
    for ad in results:
        print(ad)




if __name__ == '__main__':
    main()

# Добавить общую функцию или для вызова остального более простым способом
