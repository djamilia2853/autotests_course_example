# задача 1
square_side = 5
perimeter = 4 * square_side
square_area = square_side ** 2
square_diagonal = square_side * (2 ** 0.5)
print('Результат задачи 1:')
print(f'Периметр квадрата равен {perimeter}, площадь равна {square_area}, диагональ равна {square_diagonal}')

# задача 2
a = 2
b = 6
c = 3
discriminant = b ** 2 - 4 * a * c
x1 = (- b + discriminant ** 0.5) / (2 * a)
x2 = (- b - discriminant ** 0.5) / (2 * a)
print('Результат задачи 2:')
print(f'Корни квадратного уравнения равны: \nx1 = {round(x1, 2)} \nx2 = {round(x2, 2)}')

# задача 3
string1 = "Какой чудесный день "
string2 = "Такой чудесный пень"
begin_string1 = string1[:2]
begin_string2 = string2[:2]
print('Результат задачи 3:')
print(string1.replace(begin_string1, begin_string2) + string2.replace(begin_string2, begin_string1))

# задача 4
path = r'C:\Python37-32\NEWS.txt'
split_path = path.split('\\')
file_ext = split_path[-1]
file = file_ext.split('.')
disk = split_path[0]
root_folder = split_path[1]
print('Результат задачи 4:')
print(f'Название файла: {file[0]} \nНазвание диска: {disk} \nКорневая папка: {root_folder}')

# задача 5
a = 5
b = 2
c = a + b
print('Результат задачи 5:')
print(f'{a} + {b} = {c}')
c = a * b
print(f'{a} * {b} = {c}')

# задача 6
string = 'Hello World!'
print('Результат задачи 6:')
print(string[::2])

# задача 7
string1 = 'wtf'
string2 = 'brick quz jmpy veldt whangs fox'
value1 = string2.find(string1[0])
value2 = string2.find(string1[1])
value3 = string2.find(string1[2])
min_value = min(value1, value2, value3)
max_value = max(value1, value2, value3) + 1
print('Результат задачи 7:')
print('Срез минимальной длины: ', string2[min_value:max_value])
