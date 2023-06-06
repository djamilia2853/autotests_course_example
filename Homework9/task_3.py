# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases


purchases = []
with open(r'test_file\task_3.txt', mode='r', encoding='utf-8') as f:
    purchase = 0
    for line in f:
        if line == '\n':
            purchases.append(purchase)
            purchase = 0
        else:
            purchase += int(line)

purchases = sorted(purchases, reverse=True)
three_most_expensive_purchases = sum(purchases[:3])

assert three_most_expensive_purchases == 202346
