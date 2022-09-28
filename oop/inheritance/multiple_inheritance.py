#Multiply Inheritance
#Множественное наследование
"""
В других языках нету множественное наследование Java C++ (классы наследуется только одного класса предков
- но в этих языках сущетсвует как концепция интерфейс. Инфтерфейсы похожи классами поэтому может множественно наследоваться от интерфейса)
"""

class Plavat:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Привет меня зовут {self.name} и я могу плавать")

    def swiming(self):
        print("Я могу плавать")


class Hodit:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Привет меня зовут {self.name} и я могу ходит")

    def hodit(self):
        print("Я могу ходит")


class Letet:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Привет меня зовут {self.name} и я могу летать")

    def letet(self):
        print("Я могу летать")

class PersonajIgry(Plavat, Hodit, Letet):
    def __init__(self, name):
        self.name = name
        Plavat.__init__(self,name)
        Hodit.__init__(self,name)
        Letet.__init__(self,name)

    def greeting(self):
        print(f"Привет меня зовут {self.name}")


alex = PersonajIgry(name="Alexander")
alex.greeting()
alex.swiming()
alex.hodit()
alex.letet()

print(isinstance(alex, Plavat))#Является ли объект alex объектам класса Letet
print(isinstance(alex, Letet))
print(isinstance(alex, Hodit))
print(isinstance(alex, PersonajIgry))
print(isinstance(alex, dict))

help(PersonajIgry)
print(PersonajIgry.__mro__)


class Test(PersonajIgry):
    def __init__(self, name):
        self.name = name
        PersonajIgry.__init__(self,name)
        Plavat.__init__(self, name)
        Hodit.__init__(self, name)
        Letet.__init__(self, name)

    def greeting(self):
        print(f"Привет меня зовут {self.name}")

testt = Test(name="TESTTTTTTTT")
print(testt.name)
help(testt)