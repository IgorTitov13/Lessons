# # Задание 1

"""
example1 = Насколько проще было бы писать программы, если бы не заказчики
example2 = 640Кб должно хватить для любых задач. Билл Гейтс (по легенде)
"""

input_phrase_1 = input('Введите Фразу 1')
input_phrase_2 = input('Введите Фразу 2')

if len(input_phrase_1) > len(input_phrase_2):
    print('Фраза 1 длиннее фразы 2')

elif len(input_phrase_1) < len(input_phrase_2):
    print('Фраза 2 длиннее фразы 1')

else:
    print('Фразы равной длины')

# Задание 2

input_year = int(input('Введите год'))

if (input_year % 4 == 0 and input_year % 100 != 0) or input_year % 400 == 0:
    print('Високосный год')

else:
    print('Обычный год')


# Задание 3
day = int(input('Введите день'))
month = int(input('Введите месяц'))

if (day >= 21 and day <= 31 and month == 3) or (day >=1 and day <= 19 and month == 4):
    print("Ваш знак зодиака: Овен")

elif (day >= 20 and day <= 30 and month == 4) or (day >= 1 and day <= 20 and month == 5):
    print("Ваш знак зодиака: Телец")

elif (day >= 21 and day <= 31 and month == 5) or (day >= 1 and day <= 20 and month == 6):
    print("Ваш знак зодиака: Близнецы")

elif (day >= 21 and day <= 30 and month == 6) or (day >= 1 and day <= 22 and month == 7):
    print("Ваш знак зодиака: Рак")

elif (day >= 23 and day <= 31 and month == 7) or (day >= 1 and day <= 22 and month == 8):
    print("Ваш знак зодиака: Лев")

elif (day >= 23 and day <= 31 and month == 8) or (day >= 1 and day <= 22 and month == 9):
    print("Ваш знак зодиака: Дева")

elif (day >= 23 and day <= 30 and month == 9) or (day >= 1 and day <= 22 and month == 10):
    print("Ваш знак зодиака: Весы")

elif (day >= 23 and day <= 31 and month == 10) or (day >= 1 and day <= 21 and month == 11):
    print("Ваш знак зодиака: Скорпион")

elif (day >= 22 and day <= 30 and month == 11) or (day >= 1 and day <= 21 and month == 12):
    print("Ваш знак зодиака: Стрелец")

elif (day >= 22 and day <= 31 and month == 12) or (day >= 1 and day <= 19 and month == 1):
    print("Ваш знак зодиака: Козерог")

elif (day >= 20 and day <= 31 and month == 1) or (day >= 1 and day <= 18 and month == 2):
    print("Ваш знак зодиака: Водолей")

elif (day >= 19 and (day <= 28 or day <= 29) and month == 2) or (day >= 1 and day <= 20 and month == 3):
    print("Ваш знак зодиака: Рыбы")

else:
    print('День или месяц введены некорректно')

Задание 4

width = 10
length = 205
height = 5

if width < 15 and length < 15 and height < 15:
    print('Коробка №1')
elif (width > 15 and width < 50) or (length > 15 and length < 50) or (height > 15 and height < 50):
    print('Коробка №2')
elif length > 200:
    print('Упаковка для лыж')
else:
    print('Стандартная коробка №3')
