#Цикл for
"""
Очень часто в программировании возникает потребность перебрать какой то элемента последовательности
и произвости какой то действие над каждом элементом или каким то выбранным из элементом
"""
"""
Көп учурда программалоодо ырааттуулуктун кандайдыр бир элементин кайталоо зарылчылыгы бар
жана ар бир элементке же айрым тандалган элементке кандайдыр бир аракеттерди аткарыңыз
"""
#for переводится для - үчүн
numbers_list = [1,2,3,4,5]
for numbers in numbers_list:
    print(numbers)

for print_hi in numbers_list:
    print("Hi")
    print(print_hi)
    print(str(print_hi) + " hello")

#Не обезательно мы может все элементы выводить
# Биз бардык элементтерди көрсөтө алабыз деп айтууга болбойт
for numbers in numbers_list:
    if numbers % 2 == 0:
        print(numbers)
    print("Hi")

#Вычисление элемента
list_numbers_summ = 0
for numbers in numbers_list:
    list_numbers_summ = list_numbers_summ + numbers
    print(list_numbers_summ)#Здесь показывается каждый прибавление
print(list_numbers_summ)#Здесь показывается общий результат вычислений

#Работа с строками
stroka_salamdashuu = "Hello Python"
for stroka in stroka_salamdashuu:
    print(stroka)

for stroka in stroka_salamdashuu:
    if stroka == "l":
        print(stroka)

for stroka in stroka_salamdashuu:
    if stroka != "l":
        print(stroka)

for stroka in "Hello Python":
    if stroka == "l":
        print(stroka)

for stroka in "Hello World!":
    print("One more time")

turple_list = [(1,2),("a","b"),(2,3),("c","d"),("e","f")]
for item in turple_list:
    print(item)

for example_one, example_two in turple_list:
    print(example_one, example_two)
    print(example_one)

dictionary_example = {"key":"value", "key1":"value1","key2":"value2","key3":"value3"}
for item in dictionary_example:
    print(item)

for item in dictionary_example.items():
    print(item)

for item in dictionary_example.keys():
    print(item)

for item in dictionary_example.values():
    print(item)

for key, value in dictionary_example.items():
    print(key)

for key, value in dictionary_example.items():
    print(value)

for item in range(5):
    print(item)

x = range(3, 6)
for n in x:
    print(n)

for item in range(3, 20, 2):
    print(item)