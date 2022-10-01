

# __name__ = "__main__"
print(__name__)

def function_one():
    print("function_one from first.py")
print("Top level in first.py")

def function_two():
    pass

class MyClass:
    pass



if __name__ == '__main__': #Проверяем действительно ли этот модуль или питон файл запущен
    # самостоятельно а не импортирован ли и потом исполняем какойто код
    # function_one()
    # function_two()
    print("first.py is being run directly")
else:
    print("first.py has been imported")