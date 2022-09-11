#Список Питоне
"""
#Как вы помните упорядоченная последовательность объектов которой можно указать в квадратном скобках
#Эсиңде болсо, объекттердин иреттелген ырааттуулугу төрт бурчтуу кашаанын ичинде көрсөтүлүшү мүмкүн
"""

number_list = [123,13,434,322,222]#Список - Тизмелер
print(number_list)
some_list = [123, 3, 444, 4.4, "hello"]
print(some_list)
print(len(some_list))#Здесь уточняем длину списка (В результате получаем 5 элементов)
print(len(some_list))#Бул жерде биз тизменин узундугун көрсөтөбүз (Натыйжада биз 5 элементти алабыз)

"""Как вы помните строках точно так в  списке мы можем  применять индексацию и вырезание"""
"""Эсиңде болсо, тизмедеги саптар так ошондой, биз индекстөө жана кесүүнү колдоно алабыз"""

#Индексация
print(some_list[0])

#Slicing - вырезания
another_list = some_list[:3]
print(another_list)

"""Как вы помните строки были не меняемым - Списке нету такого проблемы нет"""
"""Эсиңерде болсо, саптарда өзгөртууго мумкун эмес - тизмеде мындай көйгөй жок"""
some_list[4] = "Good Bye"
print(some_list)

"""В списке можем конкентинацию""" """Тизмеде биз бириктире алабыз"""
new_list = some_list + another_list
print(new_list)

"""Мы можем добавлять новый элемент""" """Биз жаңы элемент кошо алабыз"""
new_list[7] = "new item"
print(new_list)
new_list.append("func append")
print(new_list)
new_list.insert(0,'inserted and added new elements')
print(new_list)

"""Удаление элементов в списке""" """Тизмедеги нерселерди жок кылуу"""
new_list.pop()#Удаляет последний элемент по умолчанию -1 (#Демейки боюнча акыркы элементти жок кылат -1)
new_list.pop(0)
deleted_item_return_variables = new_list.pop()
print(deleted_item_return_variables)
deleted_item_return_variables = new_list.remove(123)
print(deleted_item_return_variables)

"""Сортирование списка """ """Тизмени сорттоо """
number_list_two = [1233,4546,76565,-3,0,454,6666,777,-66]
character_list = ['a','d','h','r']
number_list_two.sort()
character_list.sort()
print(number_list_two)
print(character_list)

"""Выстраивание элементы обратном порядке """ """Элементтерди тескери тартипте жайгаштырыңыз"""
number_list_two.reverse()
character_list.reverse()
print(number_list_two)
print(character_list)

number_list_two.append(character_list)
print(number_list_two)