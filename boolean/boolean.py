#Boolean значение и операторы сравнение
#Boolean значение бывает True и False
print(type(True))
print(type(False))
#Boolean мааниси True жана False болушу мүмкүн
#Чаше всего мы сравниваем два или более значений

#Операторы сравнение
#Салыштыруу операторлору

#Равно  ==
print(1 == 1)
print(1 == 2)
print("Hello" == "Hello")
print("hello" == "Hello")
print(1 < 2)

#Не Равно !=
print(1 != 1)
print(1 != 2)
print("Hello" != "Hello")
print("hello" != "Hello")

#Больше
print(1 > 2)

#Меньше
print(1 < 2)

#Больше и равно
print(1 >= 2)
print(2 >= 2)
print(3 >= 2)

#Меньше и равно
print(1 <= 2)
print(2 <= 2)
print(3 <= 2)

#Также можем сравнить строки. Строки сравнивается по символьно
#У каждого символа есть ASCII (Числовой код для каждого символа)
print(ord("A"))
print(ord("a"))
print(ord("я"))
print(ord("Я"))
print("a" == "a")
print("A" == "a")
print("A" >= "A")
print("A" >= "a")
print("A" <= "a")
print("Hi" == "Hello")
print("Hi" >= "Hello")

x = 10
y = 20
print(x == y)
print(x > y)
print(x >= y)
print(x < y)

# age = input("Укажите ваше возраст")
# print("Ваш возраст " + str(age))
# print("Ваш возраст разрешен для дальнейшего пользования " + age >= 18)
age1 = int(input("Укажите ваше возраст"))
# print("Ваш возраст разрешен для дальнейшего пользования " + age1 >= 18)
print("Ваш возраст разрешен для дальнейшего пользования " + str(age1 >= 18))

