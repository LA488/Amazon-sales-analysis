import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('amazon.csv')

# 3. Быстрый обзор данных
print("Размер данных:", df.shape)  # сколько строк и столбцов
print("\nПервые 5 строк:\n", df.head())  # первые строки
print("\nИнформация по столбцам:\n")
print(df.info())  # типы данных и пропуски

# 4. Основные статистики для числовых столбцов
print("\nОписание данных:\n", df.describe())

# 5. Проверка пропусков в данных
print("\nПропуски в столбцах:\n", df.isnull().sum())
