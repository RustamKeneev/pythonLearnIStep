#Логические операторы
#logical_operators

x = 1
y = 2

#нам нужно сравнить
print(x > 1)
print(y > 1)

#Чтобы узнать истинно бы ли оба выражений нужен логический операторы
#Логические операторы and, or. not

#and
print(x > 1 and y > 1)
print(x >= 1 and y >= 1)

#or
print(x > 1 or y > 1)

#not
print(not x > 1)
print(not y > 1)

print(True and True)
print(True or True)
print(not True)

print(False and False)
print(False or False)
print(not False)

print(True and False)
print(True or False)

name = "Jack"
age = 21
is_study_it = False
text_sorry = "К сожалению"
text_please = "С удовольствием "
have_money_to_study = False
have_to_laptop = False
if age > 18 and is_study_it == False:
    print("Привет {}Добро пожаловать курсы программирование".format(name))

if age > 18 and is_study_it == False and have_money_to_study == False:
    print("{} {} найдите денги для курсы программирование".format(name, text_sorry))

if age > 18 or is_study_it == False and have_money_to_study == False:
    print("{} {} найдите денги для курсы программирование".format(name, text_sorry))