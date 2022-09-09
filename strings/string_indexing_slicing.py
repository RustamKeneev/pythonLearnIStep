#Индексация и вырезание строк
#Индекстөө жана саптарды чечип алуу

"""
# Как вы помните строка это упорядачная последевательность символов
# Сиз эсиңизде болсок, сап символдордун иреттелген ырааттуулугу
#Каждый символ стоит опреледенной позиции, позиция начиается с нуля
# Ар бир символдун өзгөчө позициясы бар, орду нөлдөн башталат
"""

salamdashuu = "Hello Python"
salamdashuu_ozgormonun_uzundugu = len(salamdashuu)
print(salamdashuu_ozgormonun_uzundugu)

#Indexing
#Получение индексации
print(salamdashuu[0])
print(salamdashuu[7])
"""Мы можем достать строки с конца указав -1"""
print(salamdashuu[-1])


#Slicing
#Вырезание кусочек строки
print(salamdashuu[1:5])
print(salamdashuu[7:11])
print(salamdashuu[-8:-2])
print(salamdashuu[2:])
print(salamdashuu[-2:])
print(salamdashuu[:5])
print(salamdashuu[:])
print(salamdashuu[::2])
print(salamdashuu[1::3])
print(salamdashuu[::-1])#Стока перевернется