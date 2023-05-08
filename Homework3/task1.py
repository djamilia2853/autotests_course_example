# Напишите функцию modification(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.

def modification(lst):
    # Здесь пишем код
    new_begin = lst.pop(-1)
    new_end = lst.pop(0)
    lst.insert(0, new_begin)
    lst.append(new_end)
    return lst

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    ['н', 'л', 'о', 'с']
]

test_data = [
    [3, 2, 1], [5, 2, 3, 4, 1], ['с', 'л', 'о', 'н']
]


for i, d in enumerate(data):
    assert modification(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
