#Встроенные модули
#Built-in modules
"""
Модуль - это файл python кодом, тоесть каждый файл которые мы писали программу какойто это является модулем.
написанное модуля можем дальнейщем использовать (Например мы писали какойто функции и мы хотим использовать в другом
python файле не обезательно заново переписывать новый функцию еще раз - мы при таком ситуации можем пользовать модуль
котором была создана это функция)

Питоне много встроенные готовые модули (random shuffle и др)
https://docs.python.org/3/tutorial/modules.html

https://docs.python.org/3/py-modindex.html
"""

import random
x = random.randint(1, 20)
print(x)

from random import randint
y = randint(1, 300)
print(y)

my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)
