#Упавление ошибками
# print("Some code")
# print(peremennaya)
# print("Dalshe dsfsdfsdfsd")

# print("Какой то код до ошибки")
# try:
#     print(peremennaya_two)
# except:
#     print("Найдено ощибка")
# print("Код после ошибки")

# print(len(300))
# try:
#     print(len(300))
# except NameError:
#     print("Name Error")
# except TypeError:
#     print("TypeError")

user_dictionary = {'first_name':'Rustam','second_name':'Keneev', 'age':37}
# print(user_dictionary['first_name'])
# print(user_dictionary['second_name'])
# print(user_dictionary['second'])
# print(user_dictionary.get('second_name'))
# print(user_dictionary.get('second'))

def get_dictionary_values(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        print("Ошибка ключа")
print(get_dictionary_values(user_dictionary, 'age'))
print(get_dictionary_values(user_dictionary, 'ф'))
