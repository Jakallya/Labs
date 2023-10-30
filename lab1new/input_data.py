from error_messages import *
import pandas as pd
import csv
import os

def input_file():
    return input('Введите путь к файлу:\n')

def check_file_path(file_path):
    if '.csv' not in file_path:
        return FILE_FORMAT_ERROR
    elif os.path.exists(file_path) == False:
        return NOT_EXIST_FILE_ERROR
    elif os.path.getsize(file_path) == 0:
        return EMPTY_FILE_ERROR
    else:
        return 0

def input_region():
    return input('Введите название региона:\n')

def input_column_id():
    return int(input('Введите id колонки:\n'))

def check_num_column(column_num, file):
    res = 1
    if 0 < column_num <= len(list(file[0].keys())):
        res = 0
    return res

























# def input_file():
#     file = input('Введите путь к файлу:\n')
#     if  '.csv' in file:
#         file = pd.read_csv(file, delimiter=',', names=['year','region','npg','birth_rate','death_rate','gdw','urbanization'], index_col=False)
#         pd.set_option('display.max_columns', None)
#         pd.set_option('display.max_rows', None)
#         pd.set_option('display.width', None)
#         return file
#     else:
#         print('Дубль два, вводим нормальный путь, мне еще эту лабу защищать')
#         return 1
#
# def input_region(file):
#     region_base = file['region'].unique()
#     print(region_base)
#     region = input('Введите регион:\n')
#     if region in region_base:
#         new_file = file[file['region'] == region]
#         print(new_file)
#     else:
#         print('Мы живём в России, а не в Германии, вводим наш регион')
#         return 1
#
# def input_id(file): #ГОСПОДИ, Я НЕ ЕБУ, КАК ЭТОТ ХЭДЕР НОРМ СДЕЛАТЬ
#     header = file[0]
#     id_column = input('Введите ID колонки:\n')
#     if id_column in header:
#         return 0
#     else:
#         print('Введите другой ID')
#         return 1