#Special (magic) methods __methods_name__
"""
https://docs.python.org/3/reference/datamodel.html#special-method-names
"""

x = 5
y = 3

a = "5"
b = "3"

print(x + y)
print(a + b)

print(x.__add__(y))
print(a.__add__(b))

#Создание класса
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

#Создание объекта
alex = Person(first_name="Alexdaer",last_name="Petrov", age=100)
print(len([1,2,3,4,5]))
# print(len(alex))
print(alex)
# print(alex.first_name, alex.last_name, alex.age)


class PersonTwo:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __len__(self):
        return self.first_name

    def __add__(self, other):
        return self.age + other.age

petr = PersonTwo(first_name="Petr",last_name="Petrov", age=100)
ivan = PersonTwo(first_name="Ivan ", last_name="Ivanov", age=12)
print(petr)
print(len(str(petr)))

print(petr + ivan)
