# Iterate
#Раньше мы познакомились последовательности циклом мы можем перебирать элементов какого то списков
# Iterables objects
"""
Что такое Iterable объект элемента можно которой перебирать это есть Iterable.
Iterables можно переводить перебираемый
"""
# number_list = [1, 2, 3, 4, 5]
# for item in number_list://перебирание элементов списка
#     print(item)
#
# for item in 'my string':
#     print(item)
#
# Iterators
"""
Iterators - можно переводить как переборщик или перебиратель  
Iterators - надо писать готовой функции iter
для чего используется Iterator - дело в том что в циклах например  неявно используется иттераторы
Элементы обхекты иттерации перебирается с помощью иттератора и для этого используется функция next 
"""
# number_list_iterator = iter(number_list)
# print(type(number_list_iterator))
#
# string_iterator = iter('my string')
# print(type(string_iterator))
#
# # print(number_list_iterator.__next__())
# # print(number_list_iterator.__next__())
# # print(number_list_iterator.__next__())
# # print(number_list_iterator.__next__())
# # print(number_list_iterator.__next__())
#
#
#
# # print(string_iterator.__next__())
# # print(string_iterator.__next__())
# # print(string_iterator.__next__())
# # print(string_iterator.__next__())
#
# print(next(number_list_iterator))
# print(next(number_list_iterator))
# print(next(number_list_iterator))
# print(next(number_list_iterator))
# print(next(number_list_iterator))


def my_for_loop(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            print('Iteration is finished')
            break


my_for_loop('hello')
my_for_loop([1, 2, 3])