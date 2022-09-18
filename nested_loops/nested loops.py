#Nested loops
#вложенные циклы

smile = "*"
for number in range(10):
    count = 0
    emoji = ''
    while count <= number:
        emoji += "*"
        count += 1
    print(emoji)

for number1 in range(10):
    emoji2 = ""
    for count2 in range(number1 + 1):
        emoji2 += "*"
    print(emoji2)

for number3 in range(11):
    print("*" * number3)