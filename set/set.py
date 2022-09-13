#Set - Множество - Көп
# Множество - это неупородяченная коллекция уникальных элементов (тоест множество не может
# быть одинаковых объектов)
# Көптөгөн уникалдуу элементтердин сорттолбогон жыйнагы (башкача айтканда, топтом мүмкүн эмес
# окшош объектилер болушу керек)

#Отличие от словаря множество заключается добавлением значений
#Сөздүк топтомунан айырмасы баалуулуктарды кошууда
nationals = {'kyrgyz','russian','kazah','uzbek','japan'}
print(nationals)
print(type(nationals))

#Бывает случаи мы хотим создать пустое множество
#Кээде биз бош топтом түзгүбүз келет
empty_set = {}
print(empty_set)
print(type(empty_set))# При уточнении мы получаем словарь - Такталгандан кийин сөздүк алынып калат
#Тогда будем решать в переменную будем указать явно типы данных set
#Андан кийин биз өзгөрмө боюнча чечим кабыл алабыз, биз дайындардын түрлөрүн ачык көрсөтөбүз
empty_set = set()
print(type(empty_set))

#Также мы можем создавать множестов других структуры данных например из списков, кортежа
# биз тизмелер, кортеждер сыяктуу көптөгөн башка маалымат структураларын түзө алабыз
number_list = [1, 2, 3, 4, 5]
text_tuple = ('one', 'two', 'three')
set_from_list = set(number_list)#Создадим множество на основе списка (number_list качестве параметра)
set_from_tuple = set(text_tuple)#Создадим множество на основе кортежа (text_tuple качестве параметра)
print(set_from_list)#При распечатки отмечаем каждый порядки изменяется но все элементы уникальны
print(set_from_tuple)#При распечатки отмечаем каждый порядки изменяется но все элементы уникальны

#Добавление
set_from_list.add(123)
set_from_tuple.add("four")
print(set_from_list)
print(set_from_tuple)
print(set_from_list)


#Все элементы уникальны поэтому при добавлении похожего элемента то не получаем дубликат
set_from_list.add(123)
set_from_tuple.add("four")

#Удаление - удаление происходит случайном образом
set_from_list.pop()
print(set_from_list)
set_from_list.remove(3)#Явное удаление элементов (может ошибка если нету элемента)
print(set_from_list)
set_from_list.discard(1)# при удалении нету элемента тогда ничего не произходит
print(set_from_list)
# set_from_list.remove(3)#Ошибка

set_from_list.clear()#Очищает все