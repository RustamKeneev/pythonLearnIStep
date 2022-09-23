#Method Resolution Order
#Порядок разрешения метода


#   A
#  / \
# B   C
#  \ /
#   D

class A:
    def some_method(self):
        print("Method of class A")


class B(A):
    def some_method(self):
        print("Method of class B")


class C(A):
    def some_method(self):
        print("Method of class C")


class D(B, C):
    def some_method(self):
        print("Method of class D")

some_object = D()
some_object.some_method()

class A2:
    def some_method(self):
        print("Method of class A")


class B2(A2):
    pass
    # def some_method(self):
    #     print("Method of class B")


class C2(A2):
    def some_method(self):
        print("Method of class C")


class D2(B2, C2):
    pass
    # def some_method(self):
    #     print("Method of class D")

some_object_two = D2()
some_object_two.some_method()
print(D2.__mro__)#Проверка иерхатических порядок наследований
print(D2.mro())#Проверка иерхатических порядок наследований
help(D2)#Проверка иерхатических порядок наследований