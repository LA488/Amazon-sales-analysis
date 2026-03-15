import os
import shutil

# Определение путей
base_dir = r"d:\My projects\Amazon Sales"
data_dir = os.path.join(base_dir, "data")
notebooks_dir = os.path.join(base_dir, "notebooks")

# Создание директорий
os.makedirs(data_dir, exist_ok=True)
os.makedirs(notebooks_dir, exist_ok=True)

# Перемещение файлов
try:
    if os.path.exists(os.path.join(base_dir, 'amazon.csv')):
        shutil.move(os.path.join(base_dir, 'amazon.csv'), os.path.join(data_dir, 'amazon.csv'))
        print("amazon.csv moved")
except Exception as e:
    print(f"Error moving amazon.csv: {e}")

try:
    if os.path.exists(os.path.join(base_dir, 'amazon_eda.ipynb')):
        shutil.move(os.path.join(base_dir, 'amazon_eda.ipynb'), os.path.join(notebooks_dir, '01_amazon_eda.ipynb'))
        print("amazon_eda.ipynb moved")
except Exception as e:
    print(f"Error moving amazon_eda.ipynb: {e}")

try:
    if os.path.exists(os.path.join(base_dir, 'main.py')):
        shutil.move(os.path.join(base_dir, 'main.py'), os.path.join(notebooks_dir, '00_initial_script.py'))
        print("main.py moved")
except Exception as e:
    print(f"Error moving main.py: {e}")
    
print("Structure setup complete.")
