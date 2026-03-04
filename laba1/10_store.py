#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе

# Лампа
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Стол
table_code = goods['Стол']
tables_items = store[table_code]
tables_total_quantity = tables_items[0]['quantity'] + tables_items[1]['quantity']
tables_total_cost = (
    tables_items[0]['quantity'] * tables_items[0]['price'] +
    tables_items[1]['quantity'] * tables_items[1]['price']
)
print('Стол -', tables_total_quantity, 'шт, стоимость', tables_total_cost, 'руб')

# Диван
sofa_code = goods['Диван']
sofas_items = store[sofa_code]
sofas_total_quantity = sofas_items[0]['quantity'] + sofas_items[1]['quantity']
sofas_total_cost = (
    sofas_items[0]['quantity'] * sofas_items[0]['price'] +
    sofas_items[1]['quantity'] * sofas_items[1]['price']
)
print('Диван -', sofas_total_quantity, 'шт, стоимость', sofas_total_cost, 'руб')

# Стул
chair_code = goods['Стул']
chairs_items = store[chair_code]
chairs_total_quantity = (
    chairs_items[0]['quantity'] +
    chairs_items[1]['quantity'] +
    chairs_items[2]['quantity']
)
chairs_total_cost = (
    chairs_items[0]['quantity'] * chairs_items[0]['price'] +
    chairs_items[1]['quantity'] * chairs_items[1]['price'] +
    chairs_items[2]['quantity'] * chairs_items[2]['price']
)
print('Стул -', chairs_total_quantity, 'шт, стоимость', chairs_total_cost, 'руб')
