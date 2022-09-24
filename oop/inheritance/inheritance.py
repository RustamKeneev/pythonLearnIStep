#Inheritance - Наследование

class Car:
    colesa = 4

    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year
        print("Car is created")

    def car_driving(self, city):
        print(self.name + "Car begin driving " + city)

    def change_color(self, new_color):
        self.color = new_color
        print("Color is changed " + new_color)

#Создание потомок класса Car
class Truck(Car):#Наследование потомка класа Car
    colesa = 12

    def __init__(self, name, color, year):#Вызываем инициализацию
        """Внутри методе __init__ мы должны вызвать метод __init__ предка класса Car"""
        Car.__init__(self,name, color, year)
        print("Truck is created")

    def car_driving(self, city):
        print("Truck is " + self.name + "Car begin driving " + city)

    def load_weight(self, weight):
        self.weigth = weight
        print("loaded " + str(weight))


kamaz = Truck(name='Kamaz 2,0 ',color="Blue", year=2020)
print(kamaz.name, kamaz.color, kamaz.year)
kamaz.car_driving("Bishkek")
print(kamaz.colesa)
kamaz.load_weight(2000)


class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def get_info_city(self):
        print("City: ", self.name, "latitude: ", self.latitude, "longitude: ", self.longitude)


class Bishkek(City):
    naselenie = 0
    def __init__(self, naselenie, name, latitude, longitude):
        super(Bishkek, self).__init__(name,latitude, longitude)
        self.naselenie = naselenie

bishkek = Bishkek(naselenie=1000000, name="Bishkek", latitude=42.344, longitude=32.3222)
bishkek.get_info_city()