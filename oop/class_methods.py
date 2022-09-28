
class Gamer:
    active_gamers = 0
    def __init__(self,nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adults_level_permission(self):
        if self.is_adult():
            print("You can adult to level")
        else:
            print("Not adult")

gamer_one = Gamer("Rustam",20, "10",202)
gamer_two = Gamer("SSSS",21, "12",2302)
gamer_three = Gamer(nickname="sdsada",age=12, level=122222,points=1222)

print(gamer_one.get_age())
gamer_one.get_adults_level_permission()
print(gamer_one.get_nickname())


print(gamer_two.get_age())
gamer_two.get_adults_level_permission()
print(gamer_three.get_nickname())
print(gamer_three.get_age())
print(gamer_three.is_adult())
print(gamer_three.get_level())
