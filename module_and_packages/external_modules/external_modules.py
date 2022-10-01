# Внешние модули
"""
Файлы написаны питоне файле которые написаны другими программистами которой размещенное в сети интернет
python external modules and packages
https://pypi.org/
https://pypi.org/search/

termcolor
"""

import termcolor
print("Hellooeerrrr")
print(termcolor.colored("gegegegegegeggegeg", "red"))
print(termcolor.colored("Hello term color", "green"))
print(termcolor.colored("Hello term color", "green", "on_red"))
# help(termcolor)

import gtts
from playsound import playsound


def say_hello():
    tts = gtts.gTTS("Кандайсын Rustam Aka Откройте новый файл Python и импортируйте", lang="ru")
    tts.save("say_hello.mp3")
    playsound("say_hello.mp3")


say_hello()
