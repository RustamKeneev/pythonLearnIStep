

#function - функции
"""Кусок кода которая выполняет какойто функциональность и назнванием именем и
пишем имя вызывается кусок кода которая реализует вывода  функиональность параметра или без  которой мы
передаем в функцию"""

#print готовый функция python

#Встроенные функции
x = print("Hello world")
y = set()
print(type(x))
print(type(y))
print(x)
print(y)

#Встроенные методы
"""
Методы это другое название функции - это функция которое существует у объектов 
"""
some_list = [1,2,4,5,6,7]
some_list.append(8)#Метод с параметрами
print(some_list)
some_list.clear()#Метод без параметра

""" Ссылка на документацию про Python
https://docs.python.org/3/library/index.html
"""

#Функции создается с ключевым словом def
# define - Oпределять -

#Функция без параметра
def salamdashuu():#Отличие от переменнных название функции заключается открываюшей и закрывающей скобкой
    """
    Это функция просто распечетает и ничего не возврашает
    Doc string - вызывается тремя ковычками - док стринг описывает о функции
    :return: None - ничего не возращает
    """
    print("Hello")

#Вызов функции
salamdashuu()

#Описание о функции с помощью help
help(salamdashuu)

#Функция c параметрами
def sayHelloByName(name):
    """
    :param name: name
    :return: None
    """
    print("Hello " + name)
sayHelloByName("Rustam")

def sayHelloByNameTwo(name='Name'):#Чтобы не было ошибки формально укажем параметру
    """
    :param name: name
    :return: None
    """
    print("Hello " + name)
sayHelloByNameTwo()#Фактически указываем без значение параметров
sayHelloByNameTwo("Rustam")

#Возврашаемые функции
def sum_two_numbes(a, b):
    pass

def sum_two_numbes_two(a=0,b=0):
    """
    :param a: first parameter
    :param b: second parameter
    :return: a + b return results two summ
    """
    return a + b

def find_hello_tex(text):
    if "hello" in text:
        return True
    else:
        return False
find_hello_tex("Hello Mottor")

def is_string_in_text(string, text):
    """
    :param string:
    :param text:
    :return: string in text
    """
    return string in text
print(is_string_in_text("l", "World"))

def gender_text(name, gender):
    if gender == "male":
        print("Hello " + name + " your gender Man")
        return gender
    elif gender == "female":
        print("Hello " + name + " your gender Female")
        return gender
    else:
        print("Hello " + name + "I dont known your gender")
returned_value = gender_text('John','male')






"""
Как преобразовать текст в речь в Python
# Для начала установим необходимые модули:
pip3 install gTTS pyttsx3 playsound
"""

"""
Преобразование текста в речь онлайн
#Как вы можете догадаться, gTTS означает Google Text To Speech, это библиотека 
Python для взаимодействия с API преобразования текста в речь Google Translate. Для этого требуется подключение к 
Интернету, и он довольно прост в использовании.
"""

"""
Откройте новый файл Python и импортируйте:
import gtts
from playsound import playsound
"""
import gtts
from playsound import playsound
def sayHello():#Отличие от переменнных название функции заключается открываюшей и закрывающей скобкой
    print("Hello")
    # make request to google to get synthesis
    tts = gtts.gTTS("Кандайсын Rustam Aka Откройте новый файл Python и импортируйте",lang="ru")
    # save the audio file
    tts.save("hello.mp3")
    # play the audio file
    playsound("hello.mp3")
sayHello()

