#Способы форматирование строк
print(1 + 2)
print("22" + "22")
age = 100
# print("Alexander is" + age + "years old.")
print("Alexander is" + str(age) + "years old.")

name = "Alexander"
age2 = 100
name_and_age = 'My name is{0} i\'m {1} years old'.format(name, age)
print(name_and_age)

name_and_age = 'My name is{0} i\'m {1} years old'.format("Alexander", 100)
print(name_and_age)

name_and_age_two = f'My name is{name} i\'m {age} years old'
print(name_and_age_two)



#Если много параматеров
week_days = "В неделе 7 дней: {},{},{},{},{},{},{}"\
    .format("Понедельник","Вторник","Среда","Четверг","Пятница", "Суббота","Воскресенье")
print(week_days)

week_days_two = "В неделе 7 дней: {1},{6},{0},{4},{2},{3},{5}"\
    .format("Среда","Понедельник","Пятница", "Суббота","Четверг","Воскресенье","Вторник")
print(week_days_two)

week_days_three = "В неделе 7 дней: {ponedelnik},{vtornik},{sreda},{chetverg},{pytnica},{subbota},{voskresenie}"\
    .format(ponedelnik="Понедельник", vtornik="Вторник",sreda="Среда",chetverg="Четверг",pytnica="Пятница",
            subbota="Суббота", voskresenie="Воскресенье")
print(week_days_three)

float_result = 1000 / 7
print(float_result)
print("The result division is {0}".format(float_result))
print("The result division is {0:1.3f}".format(float_result))

#Python 2 version
print("My name is %s. %s %d years old "%(name, "Im", age))