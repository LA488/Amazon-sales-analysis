# Amazon Sales Analysis - Jupyter Notebook Version

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 📥 Загрузка и подготовка данных
df = pd.read_csv("amazon_sales.csv")

df['discounted_price'] = df['discounted_price'].str.replace("\u20b9", "").str.replace(",", "").astype(float)
df['actual_price'] = df['actual_price'].str.replace("\u20b9", "").str.replace(",", "").astype(float)
df['discount_percentage'] = df['discount_percentage'].str.replace("%", "").astype(float)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce').fillna(0)
df = df.dropna(subset=['rating'])

# ---------------------------- Анализ и Визуализация ----------------------------

# 📊 Распределение по категориям
category_counts = df['category'].value_counts().head(10)
sns.barplot(
    x=category_counts.values,
    y=category_counts.index,
    hue=category_counts.index,
    palette="viridis",
    legend=False
)
plt.title("Топ-10 категорий товаров по количеству")
plt.xlabel("Количество товаров")
plt.ylabel("Категория")
plt.tight_layout()
plt.show()

# ⭐ Средний рейтинг по категориям (топ-10)
category_rating = df.groupby("category")["rating"].mean().sort_values(ascending=False).head(10)
sns.barplot(
    x=category_rating.values,
    y=category_rating.index,
    hue=category_rating.index,
    palette="mako",
    legend=False
)
plt.title("Средний рейтинг по категориям (топ-10)")
plt.xlabel("Средний рейтинг")
plt.ylabel("Категория")
plt.tight_layout()
plt.show()

# 💸 Связь между скидкой и рейтингом
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="discount_percentage", y="rating", hue="category", legend="brief")
plt.title("Связь между скидкой и рейтингом товара")
plt.xlabel("Скидка (%)")
plt.ylabel("Рейтинг")
plt.legend(bbox_to_anchor=(0.5, -0.25), loc='upper center', borderaxespad=0., ncol=3)
plt.tight_layout()
plt.show()

# 📉 Топ-10 товаров с наименьшим количеством отзывов
least_reviewed = df.sort_values(by='rating_count').head(10)
plt.figure(figsize=(10, 6))
sns.barplot(data=least_reviewed, x='rating_count', y='product_name', color='salmon')
plt.title('Топ-10 товаров с наименьшим числом отзывов')
plt.xlabel('Количество отзывов')
plt.ylabel('Название товара')
plt.subplots_adjust(left=0.3, right=0.95, top=0.9, bottom=0.1)
plt.show()

# 👎 Топ-10 товаров с самым низким рейтингом
lowest_rated = df.sort_values(by='rating').head(10)
plt.figure(figsize=(10, 6))
sns.barplot(data=lowest_rated, x='rating', y='product_name', color='tomato')
plt.title('Топ-10 товаров с самым низким рейтингом')
plt.xlabel('Рейтинг')
plt.ylabel('Название товара')
plt.subplots_adjust(left=0.3, right=0.95, top=0.9, bottom=0.1)
plt.show()

# ---------------------------- Выводы и Рекомендации ----------------------------

print("""
🔍 Выводы:
- Некоторые категории значительно популярнее других (например, Electronics, Clothing)
- Высокий рейтинг не всегда связан с размером скидки
- Много товаров имеют низкий рейтинг или почти нет отзывов

✅ Рекомендации:
- Увеличить маркетинг для товаров с хорошим рейтингом, но низкими отзывами
- Пересмотреть товары с большими скидками, но низкими оценками
- Сфокусироваться на топовых категориях для увеличения продаж
""")
