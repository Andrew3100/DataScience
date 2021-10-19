import numpy as np
import pandas as pd
import os
import math as m
import matplotlib
import matplotlib.pyplot as plt

# import seaborn as sns
AH = pd.read_csv('tips.csv', sep=",", header=0, index_col=False)

# Сколько мужчин и сколько женщин заплатили чаевые?
print('Вопрос №1. Сколько мужчин и сколько женщин заплатили чаевые?')
print()
print(str((AH['sex'][AH['tip'] > 0].value_counts()['Male'])) + ' мужчин заплатили чаевые')
print(str((AH['sex'][AH['tip'] > 0].value_counts()['Female'])) + ' женщин заплатили чаевые')

print()
# Определите долю курящих среди мужчин и женщин.
print('Вопрос №2. Определите долю курящих мужчин и женщин')
print()
# Доля курящих мужчин
print(('Доля курящих мужчин равна ' + str(round(AH['sex'][AH['smoker'] == 'Yes'].value_counts()['Male'] / AH['sex'].value_counts()['Male'], 2))))
# Доля курящих женщин
print(('Доля курящих женщин равна ' + str(round(AH['sex'][AH['smoker'] == 'Yes'].value_counts()['Female'] / AH['sex'].value_counts()['Female'], 2))))

print()

print(AH['size'][AH['day'] == 'Sun'].mean())

