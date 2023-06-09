# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime

def func_log(file_log=r'test_file\log.txt'):
    """
    Декоратор предназначенный для логирования названия и времени вызова функции.
    :param file_log: Исходный путь до txt файла.
    :return: записывает время выполнения и название функции в txt файл.
    """

    def name(funk_name):
        def wrapper():
            with open(file_log, mode='a', encoding='utf-8') as file:
                current_time = datetime.datetime.now()
                format_current_time = current_time.strftime('%d.%m %H:%M:%S')
                file.writelines(f'{funk_name.__name__} вызвана {format_current_time}\n')
            funk_name()
        return wrapper
    return name


@func_log()
def func1():
    pass


@func_log(file_log=r'test_file\func2.txt')
def func2():
    pass


func1()
func2()
func1()
