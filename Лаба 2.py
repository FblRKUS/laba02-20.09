# 1
c_1 = int(input('Сумма вклада 1: '))
c_2 = int(input('Сумма вклада 2: '))
c_3 = int(input('Сумма вклада 3: '))
S = (c_1 + c_2 + c_3) * 1.15
print(f'Общая сумма с процентами {S} руб.')

# 2
from datetime import date

today = date.today()
g = int(input('Введите год рождения: '))
v = today.year - g
if v >= 18:
    print('Вам к терапевту')
else:
    print('Вам к педиатру')

#3
c_1 = int(input('Стоимость товара 1: '))
c_2 = int(input('Стоимость товара 2: '))
c_3 = int(input('Стоимость товара 3: '))
k_1 = int(input('Количество товара 1: '))
k_2 = int(input('Количество товара 2: '))
k_3 = int(input('Количество товара 3: '))
S = (c_1 * k_1) + (c_2 * k_2) + (c_3 * k_3)
print(f'Общая сумма: {S} руб.')