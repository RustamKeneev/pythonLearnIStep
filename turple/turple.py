#Кортежи - Turple
#Кортежи похожи списку
#Кортеж inmutable тоист не можем изменить содержимое

test = 1
print(type(test))
test2 = 1,2,3,4
print(type(test2))

turple_one = (1,2,3,4,5)
print(turple_one)
turple_two = ("one","two","hello")
print(turple_two)
turple_three = (1,2,3,"hello", 4.5)
print(turple_three)

print(turple_one[0])

persone_turple = ('John','Smith', 1900)
first_name, last_name, birth_day = persone_turple
print(first_name, last_name, birth_day)

test3 = (1,2,4,5,7,88,6,88)
print(test3.count(88))
test4 = ("hello", "hi", "pooka")
print(test4.count("hi"))

print(test3.index(88))
print(test4.index("hi"))

