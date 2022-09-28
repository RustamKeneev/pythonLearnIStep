#Encapsulation
#Защита данных

class Persone:
    __name = None
    __age = None
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_info(self):
        print("Name ", self.__name, "Age ",self.__age)

class Taxist(Persone):
    staj = 0
    def __init__(self, staj, name, age):
        super(Taxist, self).__init__(name, age)
        self.staj = staj
    def get_info(self):
        super().get_info()
        print("Staj :", self.staj)

voditel = Taxist(name="Alexander",age=50, staj=3)
voditel.get_info()
voditel.staj = 5
voditel.get_info()
voditel.staj = 10
voditel.get_info()
# voditel.__name()
person = Persone(name="asdasdas", age=1222)
print(person.get_info())

