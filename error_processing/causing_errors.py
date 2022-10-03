#Causing errors
#Вызов ошибок

"""
raise - повыщать или вызвать и др.
Мы можем вызывать ощибку по нашему желанию
когда можем использовать  например написали какойто функцию которой принимает параметры строки и число
при заполнении параметром неисвестного параметра
"""

# raise ValueError("Неверное значение")
# raise ValueError()


def get_color(color_number):
    if color_number == 1:
        return "red"
    elif color_number == 2:
        return "blue"
    elif color_number == 3:
        return "black"
    elif color_number == 4:
        return "yellow"
    else:
        return "not color"


color = get_color(5)
print(color)

def raising_color(color_number):
    color_number_list = [1,2,3,4,5,6]
    if color_number not in color_number_list:
        raise ValueError("Количество цифры должны быть от 1 до 6")
    if type(color_number) is not int:
        raise TypeError("Введенное данные должны быть цифры")
    if color_number == 1:
        return "red"
    elif color_number == 2:
        return "blue"
    elif color_number == 3:
        return "black"
    elif color_number == 4:
        return "yellow"
    else:
        return "not color"

color_two = raising_color(1)
print(color_two)

def color_and_text(color_number, color_text):
    color_number_list = [1,2,3,4,5,6]
    if color_number not in color_number_list:
        raise ValueError("Параметр цифры должны быть от 1 до 6")
    if type(color_number) is not int:
        raise TypeError("Введенное параметры данные должны быть цифры")
    if type(color_text) is not str:
        raise TypeError("Параметры текста должен быть строкой")
    if color_number == 1:
        return print("red" + color_text)
    elif color_number == 2:
        return print("blue" + color_text)
    elif color_number == 3:
        return print("black" + color_text)
    elif color_number == 4:
        return print("yellow" + color_text)
    else:
        return "not color"

color_three = color_and_text(4,1)
print(color_three)