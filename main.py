import numpy as np
import pandas as pd
import colorama as color
from colorama import init, Fore
color.init()
init(autoreset=True)
import os
import math as m
import matplotlib
import matplotlib.pyplot as plt

# import seaborn as sns
AH = pd.read_csv('tips.csv', sep=",", header=0, index_col=False)

# Сколько мужчин и сколько женщин заплатили чаевые?
print(Fore.GREEN + 'Вопрос №1. Сколько мужчин и сколько женщин заплатили чаевые?')
print()
print(str((AH['sex'][AH['tip'] > 0].value_counts()['Male'])) + ' мужчин заплатили чаевые')
print(str((AH['sex'][AH['tip'] > 0].value_counts()['Female'])) + ' женщин заплатили чаевые')

print()
# Определите долю курящих среди мужчин и женщин.
print(Fore.GREEN + 'Вопрос №2. Определите долю курящих мужчин и женщин')
print()
# Доля курящих мужчин
print(('Доля курящих мужчин равна ' + str(round(AH['sex'][AH['smoker'] == 'Yes'].value_counts()['Male'] / AH['sex'].value_counts()['Male'], 2))))
# Доля курящих женщин
print(('Доля курящих женщин равна ' + str(round(AH['sex'][AH['smoker'] == 'Yes'].value_counts()['Female'] / AH['sex'].value_counts()['Female'], 2))))

print()
print(Fore.GREEN + 'Вопрос №3. В какой день недели в среднем было максимальное количество посетителей? Учитывайте размер столика?')
print()

# Пишем в массив уникальные элементы столбца DAY, так как изначально датасет содержит 4 из 7 дней недели и может быть изменён
all_days_list = AH['day'].unique()
# Перебираем массив all_days_list
for i in range(0, len(all_days_list)):
    print('В день недели ' + str(all_days_list[i]) + ' в среднем было ' + str(round(AH['size'][AH['day'] == all_days_list[i]].mean(), 1)) + ' посетителей')

print()
print(Fore.GREEN + 'Вопрос №4. На какое время суток приходится наибольшее количество чаевых?')
print()

# Та же фича, что и с днями недели а датасете, только по времени дня
all_time_list = AH['time'].unique()
for i in range(0, len(all_time_list)):
    print('Во время ' + str(all_time_list[i]) + ' в среднем было ' + str(round(AH['tip'][AH['time'] == all_time_list[i]].mean(), 1)) + ' рублей чаевых')
