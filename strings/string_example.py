#Типы данных строка (string - str)
#Строки значение указывается двойным или одинарным кавычками
"""
#Маалымат түрлөрү сап (сап - str)
#String мааниси кош же бир тырмакча менен көрсөтүлөт
"""
greeting = "Hello"
print(greeting)
first_name = "Rustam"
print(first_name)
last_name = "Keneev"
print(last_name)

spacing = " "

#Мы можем сложить и сливаться с помощью знака + с конкентинацией все переменный
"""
#Биз + белгисин колдонуп бардык өзгөрмөлөрдү кошуп жана бириктире алабыз
"""
print(greeting + first_name + last_name)
print(greeting + " " + first_name + ' ' + last_name)
print(greeting + spacing + first_name + spacing + last_name)

#Конечно мы можем в строке можеть дать значение длинную строку
"""
#Албетте, сапта узун саптын маанисин бере алабыз
"""
the_long_string = "This is the long string"
#Заметите включается или учытивается пробелы - Боштуктар кошулганына же эсептелгенине көңүл бурулат
print(the_long_string)


'''
Мы пыитаемся написать слову => 'I'm future python backend developer' при этом питон не понимает нам необходимо указать
кнаружи двойные ковычки  например решаем так "I'm future python backend developer"

Биз => 'I'm future python backend developer' деген сөздү жазууга аракет кылып жатабыз, ал эми python түшүнбөй жатат, биз такташыбыз керек
тышкы кош тырмакчалар мисалы биз ушинтип чечебиз  "I'm future python backend developer"
'''
some_string = "I'm future python backend developer"
print(some_string)
learn_python = 'I want to learn "Python"'
print(learn_python)

#Escaping \
"""
#Строку мы можем экранировать символом \
"""
some_string_one = 'I\'m future python backend developer'
print(some_string_one)
learn_python_one = "I want to learn \"Python\""
print(learn_python)

#Переход на новую строку
# Жаңы сапка өтүү
"""
#Переход на новую строку мы можем перейти  символом \n
# Символ \r  в строке если будет длинный пробелы все равно возврашает начало
# Символ \t учитивает табуляции  
"""
new_line_string = "Hello \n i am fullstack developer"
new_line_string_one = "Hello \ni am fullstack developer"
new_line_string_two = "Hello \n       \ri am fullstack developer"
print(new_line_string)
print(new_line_string_one)
print(new_line_string_two)
tabular_string = "i am\t fullstack\t developer"
tabular_number = "1231\t2323\t123123"
# tabular_number = 123\t12323213
print(tabular_string)
print(tabular_number)

#Triple quotes
string_with_triple_quotes = """This is ' text with "triple quotes" """
print(string_with_triple_quotes)