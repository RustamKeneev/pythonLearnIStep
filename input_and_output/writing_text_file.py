#Запись текстовых файлов

#Запись
# color_list = ["red","black","yellow","cyan"]
# with open('/Users/rustamkeneev/Downloads/color.txt','w') as color_text:
#     for item in color_list:
#         print(item, file=color_text)

colors = ["red","black","yellow","cyan","red","black","yellow","cyan", 112,2,2,32,332,4, True, False, 1222.3, 234242342343242342342344232]
with open('/Users/rustamkeneev/Downloads/Input/mayrambek.txt','a') as custom_color:
    # for item in colors:
    #     print(item, file=custom_color)
    print("dark green", file=custom_color)
    print("dark Ma", file=custom_color)

#Чтение
# color_list_two = []
# with open('/Users/rustamkeneev/Downloads/color.txt','r') as color_text:
#     for item in color_text:
#         color_list_two.append(item)
# print(color_list_two)

# with open('/Users/rustamkeneev/Downloads/color.txt','r') as color_text:
#     for item in color_text:
#         color_list_two.append(item.strip('\n'))
# print(color_list_two)
#
# with open('/Users/rustamkeneev/Downloads/color.txt','a') as color_text:
#     print("dark green", file=color_text)
#     print("dark blue", file=color_text)
# print(color_list_two)
