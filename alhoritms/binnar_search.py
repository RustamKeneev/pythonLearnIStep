#Бинарный поиск
# def binnary_search(list, item):
#     low = 0
#     high = len(list) - 1
#     while low <= high:
#         mid = (low + high)
#         gues = list[mid]
#         if gues == item:
#             return mid
#         if gues > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#         return None
#
# my_list = [1, 3, 5, 7, 9]
# print(binnary_search(my_list, 3))
# print(binnary_search(my_list, -1))

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_perimetr(self):
        return self.radius * 2 * 3.14

    def get_area(self):
        return 3.14 * self.radius ** 2

c1 = Circle(0)
print(c1.get_perimetr())
print(c1.get_perimetr())