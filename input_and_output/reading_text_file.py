#Чтение текстовых файлов

#Input and Output

#Input
# x = input("Input text ")
# #Output
# print("Output text " + x)

# lorem_text = open('/Users/rustamkeneev/Downloads/test.txt')
# for item in lorem_text:
#     print(item)
#     print(item, end='')
# lorem_text.close()
#
# lorem_text_two = open('/Users/rustamkeneev/Downloads/test.txt','r')
# for item in lorem_text_two:
#     print(item, end='')
# lorem_text_two.close()

# lorem_text_three = open('/Users/rustamkeneev/Downloads/test.txt','r')
# for item in lorem_text_three:
#     if "я" in item.lower():
#         print(item, end='')
# lorem_text_three.close()
#
# with open('/Users/rustamkeneev/Downloads/test.txt','r') as lorem_text_four:
#     for item in lorem_text_four:
#         if "я" in item.lower():
#             print(item, end='')
#     lorem_text_four.close()

# with open('/Users/rustamkeneev/Downloads/test.txt','r') as lorem_text_five:
#     line = lorem_text_five.readline()
#     while line:
#         print(line, end='')
#         line = lorem_text_five.readline()

# with open('/Users/rustamkeneev/Downloads/test.txt','r') as lorem_text_six:
#     text = lorem_text_six.read()
# print(text)
