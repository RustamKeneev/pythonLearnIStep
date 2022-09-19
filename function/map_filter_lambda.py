#Map, Filter and Lambda Expressions

#Лямбда выражение это быстрое способ для создание аннонимных функции
#Аннонимные функции используется один раз в момент его создания его нет имени и не можем больше пользоваться

#map
def sum_two_numbers(x):
    return x + x
number_list = [1,2,3,4,5,6,7,8,9]
result = map(sum_two_numbers, number_list)
print(result)

for item in result:
    print(item)

for item in map(sum_two_numbers, number_list):
    print(item)
print(list(map(sum_two_numbers, number_list)))

def is_string(string):
    if "a" in string:
        print("String has 'a' ")
        return True
    else:
        print("String has not 'a' ")
        return False
string_list = ['hi','name','what','hello']
print(list(map(is_string, string_list)))

#filter - встроенная функция которая работает как последовательно
#функция filter только работает функциями которая возврашает True False Boolean значение

def number_is_odd(numbers):
    return numbers % 2 == 1
number_list_two = [1,2,3,4,5,6,7,8,9]
print(filter(number_is_odd, number_list_two))
print(list(filter(number_is_odd, number_list_two)))
for item in filter(number_is_odd, number_list_two):
    print(item)

#Lambda
def cube(number):
    return number ** 3
number_list_three = [1,2,3,4,5,6,7,8,9]
print(list(map(cube, number_list_three)))

def cube_two(number):return number ** 3
print(list(map(cube_two, number_list_three)))

# lambda number: number ** 3
print(list(map(lambda number: number ** 3, number_list_three)))
print(list(filter(lambda number: number % 2 == 1, number_list_three)))