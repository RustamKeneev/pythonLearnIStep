#List_comprehension

creating = "Hello World"
some_list = []
for item in creating:
    some_list.append(item)
print(some_list)

some_list_one = [item for item in creating]
print(some_list_one)

number_list = [number for number in "1,2,3,4,5,6,7,8,9,10"]
number_list_ex = [number for number in "12345678910"]
print(number_list)

number_list_one = [num for num in range(0,10)]
print(number_list_one)
number_list_two = [num for num in range(0,10)]
print(number_list_ex)
number_list_three = [num * 3 for num in range(0,10)]
print(number_list_three)
number_list_four = [num ** 3 for num in range(0,10)]
print(number_list_four)

# number_list = [6, 43, -2, 11, -55, -12, 3, 345, 0]
# new_list = [number ** 3 / 2 for number in number_list if number > 0]
# print(new_list)
# new_list_1 = ['+' if number > 0 else '-' if number < 0
#               else 'zero' for number in number_list]
# print(new_list_1)

# # Dictionary Comprehension
# number_dict = {'first': 1, 'second': 2, 'third': 3}
# new_dict = {key: value ** 3 for key, value in number_dict.items()}
# print(new_dict)
#
# number_list = [6, 43, 0, -2, 11, -55, -12, 3, 345]
# number_dict = {number: number ** 2 for number in number_list}
# print(number_dict)
# number_dict = {number: 'positive' if number > 0
# else 'negative' if number < 0 else 'zero' for number in number_list}
# print(number_dict)

# Set Comprehension
# number_list = [6, 43, 0, -2, 11, -55, -12, 3, 345]
# number_set = {number ** 2 for number in number_list}
# print(number_set)
# number_set = {number ** 2 for number in range(3, 11)}
# print(number_set)
# letter_set = {letter.upper() for letter in 'hello'}
# print(letter_set)
