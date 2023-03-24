
titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}


store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}
# [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}]
list = ''
for item in titles:
    titles[item]
    for index in store:
        if(index ==  titles[item]):
            list += item + ' - '
            total = 0
            quantity = 0
            for quantity_and_price in store[index]:
                quantity += quantity_and_price['quantity']
                total += quantity_and_price['price'] * quantity_and_price['quantity']
            list += str(quantity) + ' шт, стоимость ' + str(total) + ' руб,\n'
                

        # store[index]






# list = "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747  руб,\n стоимость Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"




print(list)