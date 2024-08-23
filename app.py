import os
import argparse
from datetime import datetime

#Запуск приложения с аргументами: python3 app.py --path /home/dan/Desktop --name qwe

def count_files(path):
    #Подсчитывает количество файлов в заданном каталоге.
    count = 0
    for root, dirs, files in os.walk(path):
        count += len(files)
    return count

def list_top_files(path):
    #Возвращает список топ-10 файлов по размеру в указанном каталоге.
    file_sizes = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
                file_sizes.append((file_path, size))
            except OSError:
                continue
    
    # Сортируем файлы по размеру и выбираем топ-10
    file_sizes.sort(key=lambda x: x[1], reverse=True)
    return file_sizes[:10]

def print_greeting(name):
    #Выводит приветствие с указанным именем и текущей датой и временем"
    now = datetime.now()
    print(f"Привет, {name}! Текущая дата и время: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    # Определение переменной пути по умолчанию
    default_path = '/'
    
    # Параметры командной строки
    parser = argparse.ArgumentParser(description='Выполнение различных задач с файлами.')
    parser.add_argument('--path', type=str, default=default_path, help='Путь к каталогу для анализа.')
    parser.add_argument('--name', type=str, help='Имя для приветствия.')

    args = parser.parse_args()

    #Подсчет файлов
    total_files = count_files(args.path)
    print(f'Количество файлов в каталоге {args.path}: {total_files}')

    #Топ-10 файлов по размеру
    top_files = list_top_files(args.path)
    print('Топ-10 файлов по размеру:')
    for file_path, size in top_files:
        print(f'{file_path}: {size / 1024:.2f} Кб')

    #Приветствие
    if args.name:
        print_greeting(args.name)

if __name__ == '__main__':
    main()
