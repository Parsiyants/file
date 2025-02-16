from math import pi
import os

#  Задание 1
with open('recepies.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recepie_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')
            product, quantity, word = recepie
            ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
        file.readline()
        cook_book[recepie_name] = ingredients

#  Задание 2
def get_shop_list_by_dishes(dishes: list, count: int):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for product in cook_book[dish]:
                if product['product'] in result:
                    result[product['product']]['quantity'] += int(product['quantity']) * count
                else:
                    result[product['product']] = {'measure': product['measure'], 'quantity' : (int(product['quantity']) * count)}
        else:
            print('Такого блюда нет в книге')
    print(result)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3)

# Задание 3
def getSortedList(list: list):
    results = []
    for item in list:
        filePath = 'sorted/' + item
        with open(filePath, encoding='utf-8') as file:
            count = 0
            lines = []
            for line in file:
                count += 1
                lines.append(f'строка № {count} в файле {item} : {line}')
            results.append({'name' : item, 'count' : count, 'lines' : lines})
    with open('sorted/result.txt', 'w', encoding='utf-8') as file:
        file.write('')
    with open('sorted/result.txt', 'a', encoding='utf-8') as file:
        for result in sorted(results, key=lambda c: c['count']):
            file.write(result['name'] + '\n')
            file.write(str(result['count']) + '\n')
            for text in result['lines']:
                file.write(text)
            file.write('\n\n')

getSortedList(['1.txt', '2.txt', '3.txt'])