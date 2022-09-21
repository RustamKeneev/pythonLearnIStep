#Атрибуты класса
#Атрибуты описывается свойства какой того объекта тем самом мы декларируем

class Car:
    def __init__(self, name):#__init_вызывается когда создается какой объект класса
        self.name = name
        #self - Обращается вновь созданного объекту присвает его атрибуты
mercedes = Car("Mercedes")
mercedes1 = Car(name='LS 300')
print(mercedes1)
print(mercedes1.name)

class CarTwo:
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

bmw = CarTwo(name="BMW",color="Red",year=2022)
print(bmw.name,bmw.color, bmw.year)

bmw2 = CarTwo("BMW","Red",2022)
print(bmw2)

class CarThree:
    colesa = 4
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

bmw3 = CarTwo(name="BMW",color="Red",year=2022)
print(bmw3.name,bmw3.color, bmw3.year, CarThree.colesa)

cars_colesa = CarThree.colesa
print(cars_colesa)
