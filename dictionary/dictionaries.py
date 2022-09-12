#Dictionary - Словари - Сөздүктөр
"""Словари структура данных которой содержит неупородяченное последовательность объектов"""
"""Объекттердин иретсиз ырааттуулугун камтыган сөздүктөрдүн маалымат структурасы"""

"""В словарях объекты предпалагается ключ с значение. И доступ значение только по ключу"""
"""Сөздүктөрдө объекттердин мааниси бар ачкычы бар деп болжолдонот. Ал эми мааниге ачкыч аркылуу гана жетүүгө болот"""

#Ключ должен быть строкой или неизменяемым объектом а значение может быть любой объектом
#Ачкыч сап же өзгөрбөс объект болушу керек жана маани каалаган объект болушу мүмкүн
computer_prices = {'lenovo': 550, 'macbook': 1999, 'HP': 800}
print(computer_prices)

#Доступ объекта - Объектке кирүү
print(computer_prices['macbook'])
#Добавление элементов в объект - Объектке элементтерди кошуу
computer_prices['asus'] = 654
print(computer_prices)
computer_prices['lenovo'] = 200
print(computer_prices)

#Удаление
del computer_prices['HP']
print(computer_prices)

#Удаление всех элементов
computer_prices.clear()

#Часто словари пользуется для описание объектов
person = {
    'first name': 'Jack',
    'second name': 'Vorobey',
    'age': 100,
    'hobby': ['pirat','drinking jam', 'fighting'],
    'other': {'gun': 'Mech','letter':'Pencil'}
}
print(person['age'])
print(person['hobby'])
#Получение данные Хобби список
hoobies = person['hobby'] #Первый вариант
print(hoobies[2])
#Второй вариант
print(person['hobby'][2])

#Получение данные Словари внутри словаря
other = person['other'] #Первый вариант
print(other)
print(person['other']['letter'])

#Добавление данные словаря Person
person['car'] = 'Toyota'
print(person)

#Ключи словаря Person
print(person.keys())

#Значение словаря Person
print(person.values())

#Элементы словаря Person
print(person.items())





