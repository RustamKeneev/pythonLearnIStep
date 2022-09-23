#Polomorphism
#Poly-много
#Morph - форма
#Многообразный

#First
class Dog:
    def __init__(self, name):
        self.name = name

    def say(self):
        print(self.name + " is saying Wow WOW")


class Cat:
    def __init__(self, name):
        self.name = name

    def say(self):
        print(self.name + " is saying Miyayuu")

class Fish:
    def __init__(self, name):
        self.name = name


ak_tosh = Dog("Aktosh")
mishik = Cat("Tomm")
akkula = Fish(name="AKKKuuullla")

animal_list = [ak_tosh, mishik]
for item in  animal_list:
    item.say()

def animals_voice(item):
    item.say()

animals_voice(ak_tosh)
animals_voice(mishik)
# animals_voice(akkula)

#Second
class Animals:#Абстрактный объект или обобщяюший класс вних нету конкретного для реализации методов для объекта
    def __init__(self, name):
        self.name = name

    def say(self):
        """Ощибка предупреждать не имплементированных методов в классе потомков"""
        raise NotImplementedError("класс наследника должен имплементировать этот метод")

class DogTwo(Animals):
    def __init__(self, name):
        self.name = name

    def say(self):
        print(self.name + " is saying Wow WOW")


class CatTwo(Animals):
    def __init__(self, name):
        self.name = name

    def say(self):
        print(self.name + " is saying Miyayuu")

class FishTwo(Animals):
    def __init__(self, name):
        self.name = name

    def say(self):
        print(self.name + " is saying not")

ak_tosh_two = DogTwo("Aktosh 2")
mishik_two = CatTwo("Tomm 2")
akkula_two = FishTwo(name="AKKKuuullla")

animal_list_two = [ak_tosh_two, mishik_two, akkula_two]
for item in animal_list_two:
    item.say()

def animals_voice_two(item):
    item.say()

animals_voice_two(ak_tosh_two)
animals_voice_two(mishik_two)
animals_voice_two(akkula_two)