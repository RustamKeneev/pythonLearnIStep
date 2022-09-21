#Методы
#Методы - собственно говоря функции которая описывается и определяется внутри класса
# эти функции и методы выполняет какой то функциональность какие те действие
#Очень часто они выполняет действие над каким то атрибутами самого объекта внутри класса

class Car:
    colesa = 4
    def __init__(self, name, color, yaer, is_crash):
        self.name = name
        self.color = color
        self.yaer = yaer
        self.is_crash = is_crash

    #Создание методы
    def drive(self):
        print("Car is driving")
        print(self.name + " Car is driving")
    def drive_to_city(self, city):
        print("Car is driving")
        print(self.name + " Car is driving " + city)

    def change_color(self, new_color):
        self.color = new_color

#Создание объекта
mazda = Car(name="Mazda",color="red",yaer=2020,is_crash=False)
mazda.drive()
print(mazda.name, mazda.color, mazda.yaer, mazda.is_crash)
# mazda.drive_to_city()
mazda.drive_to_city("Bishkek")
mazda.change_color("Black")
print(mazda.color)

class Circle:
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius

    def get_area(self):
        return self.pi * (self.radius ** 2)

circle_one = Circle()
print(circle_one.get_area())
circle_two = Circle(radius=2)
print(circle_two.get_area())

