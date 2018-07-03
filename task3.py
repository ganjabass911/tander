"""
Задание 3
Описать декоратор для функции, выводящий название функции, переданные ей аргументы и время её выполнения
"""
import time


def decorator(func):
    def wrapper(*args):
        print(func.__name__ + "\nАргументы переданные в фунцию:")
        for arg in args:
            print(arg, end=' ')

        start_time = time.time()
        x = func(*args)
        print("\nВремя выполнения: ", (time.time() - start_time))
        return x

    return wrapper
