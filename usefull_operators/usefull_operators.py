#Встроинные функции и ключевые словах операторах языка питон довольно часто используются

#Range
for item in range(10):
    print(item)

for item in range(3,10):
    print(item)

for item in range(1,10,3):
    print(item)

print(range(5))
print(list(range(5)))

some_index = 0
some_string = "qwerty"
for item in some_string:
    print(item + " is at index " + str(some_index))
    some_index = some_index + 1

some_string_one = "qwerty"
for item in enumerate(some_string_one):
    print(item)

print("a" in "Jack")#Находиться символ а

print('x' in 'Jack')
print(str(1) in 'Jack')
print('1' in 'Jack')

letter_list = ['a', 'b', 'c', True]
print('a' in letter_list)
print(True in letter_list)

dict_1 = {1: 'a', 2: 'b', 3: 'c'}
print(1 in dict_1)
print(1 in dict_1.keys())
print(4 in dict_1.keys())
print('c' in dict_1.values())
print('z' in dict_1.values())

print(min(1, 3, 56, 4))
print(max(1, 3, 56, 4))

my_list = [1, 3, 56, 4]
print(min(my_list))
print(max('Hello'))
for letter in 'Hello':
    print(ord(letter))

from random import shuffle
my_list = [1, 3, 56, 4]
shuffle(my_list)
print(my_list)

from random import randint
print(randint(12,20))