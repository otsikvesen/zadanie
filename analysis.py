#analysis.py

import os

def get_size(path):
    """Возвращает размер файла или директории."""
    total_size = 0
    # Если это директория, проходим по всем файлам и поддиректориям
    if os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
    else:
        # Если это файл, просто получаем его размер
        total_size = os.path.getsize(path)
    return total_size

def analyze_directory(directory):
    """Анализирует размеры файлов и поддиректорий в указанной директории."""
    sizes = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        size = get_size(item_path)
        sizes.append((item, size))  # Сохраняем имя и размер в списке

    # Сортируем по размеру в порядке убывания
    sizes.sort(key=lambda x: x[1], reverse=True)

    # Выводим результаты
    for item, size in sizes:
        print(f"{item}: {size} байт")

if __name__ == "__main__":
    current_directory = os.getcwd()  # Получаем текущую директорию
    print(f"Размеры файлов и директорий в '{current_directory}':")
    analyze_directory(current_directory)

