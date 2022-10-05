# Generators are iterators
"""Генерация это есть иттераторы
при помощи генераторов мы можем перебирать какой то элементов
Не каждый генератор может быть иттератром
"""
# Generators can be created with generator functions
# Generators can be created with generator expressions
# Generator expressions - генератор выражение
# yield - уступать, выробатывать какойто значение


# def my_function(x):
#     return x
# print(my_function(4))


def count_up_to(x):
    count = 1
    while count <= x:
        yield count
        count += 1


# print(count_up_to(4))
# counter = count_up_to(4)
# # print(counter.__next__())
# # print(counter.__next__())
# # print(counter.__next__())
# # print(counter.__next__())
# # print(counter.__next__())
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

counter = count_up_to(10)
print(list(count_up_to(7)))

# for number in counter:
#     print(number)

counter.__next__()
counter.__next__()
counter.__next__()

for number in counter:
    print(number)

