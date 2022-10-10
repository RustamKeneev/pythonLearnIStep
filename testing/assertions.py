#Assertions
#Утверждения

# assert 2 + 2 == 4
# assert 2 + 3 == 4
# assert 2 + 3 == 4, '2 + 3 = 5 (результат должен быть 5)'

# def divide(a, b):
#     assert b != 0, "b не должно делиться на ноль"
#     return a / b
#
# print(divide(44, 2))
# print(divide(44, 0))


# def multiply_positive_numbers(first, second):
#     assert first > 0 and second > 0, "first и second должны быть больще нуля или положительны"
#     # print(first * second)
#     return first * second


# multiply_positive_numbers(20, 2)
# multiply_positive_numbers(20,-2)
# print(multiply_positive_numbers(20,-2))
# multiply_positive_numbers(2,0)


def get_password(password):
    password_list = [11,22,33,44,55]
    assert int(password) in password_list, 'пароль не действителен'
    print("Вы ввели правильную пароль")

passwords = input("Введите пароль")
get_password(passwords)



