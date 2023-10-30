EMPTY_FILE_ERROR = 0
FILE_FORMAT_ERROR = 1
NOT_EXIST_FILE_ERROR = 2
INPUT_REGION_ERROR = 3
ID_COLUMN_ERROR = 4
VALUE_OF_COLUMN_ERROR = 5
EMPTY_REGIONS_ERROR = 6


def output_empty_file_error():
    return print ('Файл пустой, не могу с ним работать\n')

def output_not_exist_file_error():
    return print ('Файла не существует\n')

def output_file_format_error():
    return print('Работаю только с csv файлами\n')

def output_region_input_error():
    return print('Такого региона не существует\n')

def output_id_column_error():
    return print('Неправильно введено id колонки или его нет вовсе\n')

def output_value_of_column_error():
    return print('Я не могу работать со значениями этого столбца, я могу посчитать только чиселки\n')

def output_empty_regions_error():
    return print('А регионов вообще нет, ищи другой файл\n')

def show_error_messages(error_code):
    if error_code == EMPTY_FILE_ERROR:
        output_empty_file_error()
    elif error_code == FILE_FORMAT_ERROR:
        output_file_format_error()
    elif error_code == NOT_EXIST_FILE_ERROR:
        output_not_exist_file_error()
    elif error_code == INPUT_REGION_ERROR:
        output_region_input_error()
    elif error_code == ID_COLUMN_ERROR:
        output_id_column_error()
    elif error_code == VALUE_OF_COLUMN_ERROR:
        output_value_of_column_error()
    elif error_code == EMPTY_REGIONS_ERROR:
        output_empty_regions_error()

