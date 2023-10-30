from tabulate import tabulate

from calculate_metrics import *

def print_regions(region_base):
    print ('Список регионов:\n')
    print (region_base)

def print_table(file):
    header = file[0].keys()
    table_temp = [list(a.values()) for a in file]
    table = tabulate(table_temp, header, tablefmt="grid")
    return print(table)

def print_metrics(max_value, min_value, mean_value, median_value):
    print(f'\nМакс: {max_value}')
    print(f'Мин: {min_value}')
    print(f'Среднее: {mean_value}')
    print(f'Медиана: {median_value}')

def print_percentile_table(data):
    print('Таблица перцентилей: \n')
    print (data)