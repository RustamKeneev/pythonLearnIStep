#Higher-order function
#Функция высшего порядка
"""
Higher-order function - это функция, которая может принимать в качестве аргумента другую функцию и/или
возвращать функцию как результат работы. Так как в Python функции – это объекты первого класса,
то они являются HOF, это свойство активно используется при разработке программного обеспечения.
"""

#Функция которая возвращаемое перемножение квадратов
def some_product(num, func):
    result = 1
    for item in range(1, num):
        result *= func(item)
    return result

#Функция возвращает квадрат числа
def kvadrat(x):
    return x * x

#Функция возвращает квадрат числа
def kub(x):
    return x * x * x

print(some_product(3, kvadrat))
#1 2 3

print(some_product(4, kvadrat))
#1 2 3
#1 4 9

print(some_product(4, kub))
# 1 2 3
# 1 8 27

#Работа встроенные функции

# def my_function(a, b, func):
#     result = func([a, b])
#     return result
# print(my_function(7, 3, sum))


#Работа вложенной функции
from random import choice
def colorize(chto_to):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color

    result = get_color() + ' ' + chto_to
    return result
print(colorize('apple'))

# Higher order functions, which return another function
# def make_color():
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color
#
#     return get_color

# first_color = make_color()
# print(first_color())
#
# second_color = make_color()
# print(second_color())
#
# third_color = make_color()
# print(third_color())

# Inner functions can access outer function scope
def colorize1(thing):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color + ' ' + thing

    return get_color


# print(colorize1('apple')())
colorized_dog = colorize1('dog')
print(colorized_dog())



