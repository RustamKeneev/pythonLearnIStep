#Условный оператор if elif else
#Часто используется вычисление какого то boolean выражение - тоесть выражение которое возврашает значение True или False
#Бул көбүнчө логикалык туюнтманы баалоо үчүн колдонулат, башкача айтканда, True же False кайтаруучу туюнтма.

x = 3
if x > 3:
    print("x > 3")
elif x < 3:
    print("x < 3")
else:
    print("x == 3")

svetofor = "Red"
if svetofor == "Blue":
    print("Not Blue color in svetofor")
elif svetofor == "Red":
    print("Have Red color svetofor")
elif svetofor == "Green":
    print("Have Green color svetofor")
elif svetofor == "Yellow":
    print("Have Yellow color svetofor")
else:
    print("Error")

x2 = 55
if x2 % 2 == 0:
    print('x is even')#Четный
else:
    print('x is odd')#Не Четный
    print('Some text')

user_input = input('Input something')
if user_input == 'Hello':
    print('Hello! Nice to meet you!')
    # False: 0, empty string, None, empty object
if [1, 3]:
    print('Something')

lucky_number = input('Enter a number')
if lucky_number:
    print(lucky_number + ' is your lucky number!')
else:
    print('You have to enter some number, please try again')
