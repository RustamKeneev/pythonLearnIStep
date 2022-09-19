#*args kwargs
#args (arguments)- аргументы
#**kwargs (key words argument) - аргументы по ключевому слову
# Они используется получать в качестве  параметра функции произвольно количество параметров чтобы
# не использовать болшие количество переменных при переопределении функции

#Функция которой переопределяет 10% от двух чисел
def percent_of_ten(x, y):
    return (x * y) * 0.1
print(percent_of_ten(10, 20))

def percent_of_ten(x, y,z):
    return (x * y * z) * 0.1
print(percent_of_ten(10, 20,10))

def percent_of_ten(x, y):
    return (x * y) * 0.1
# print(percent_of_ten(10, 20,20 , 20))

#*args
def percent_of_ten_with_args(*args):
    print(args)
percent_of_ten_with_args(10,2,33,44)


def percent_of_ten_with_args_two(*args):
    product = 1
    for item in args:
        product = product * item
    return product * 0.1
print(percent_of_ten_with_args_two(10,20))
print(percent_of_ten_with_args_two(10,20,20,10,1))

def percent_of_with_args(percent,*args):
    product = 1
    for item in args:
        product = product * item
    return product / 100 * percent
print(percent_of_with_args(10,20,20,20,20))

#**kwargs
def function_with_kwargs(**kwargs):
    print(kwargs)
function_with_kwargs(first=1,second=2)

def hello_with_kwargs(**kwargs):
    if "name" in kwargs:
        print("Hello good meet you {}".format(kwargs['name']))
    else:
        print("Hello whats your name")
hello_with_kwargs(gender="male",age=30, name='Alexander')
hello_with_kwargs(gender="male",age=30)

def hello_with_kwargs_two(hello,**kwargs):
    if "name" in kwargs:
        print("{} good meet you {}".format(hello, kwargs['name']))
    else:
        print("{} whats your name".format(hello))
hello_with_kwargs_two("Hi", gender="male",age=30, name='Alexander')
hello_with_kwargs_two("Good morning", gender="male",age=30, name='Alexander')
# hello_with_kwargs(gender="male",age=30)

def function_with_args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    # print("i want like {}{}".format(args[0], kwargs['first']))
function_with_args_and_kwargs(1,2,3,4, first="drink")