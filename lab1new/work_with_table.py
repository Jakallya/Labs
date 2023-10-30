import csv
from tabulate import tabulate

def get_data_from_table(csvfile):
    temp_reader = csv.DictReader(csvfile)
    return list(temp_reader)

def check_regions(file):
    res = 0
    if len(file) != 0:
        header = file[0].keys()
        if 'region' in header:
            res = 1
    return res

def get_regions(file):
    region_set = sorted(set(value['region'] for value in file))
    enumerated_list = list(enumerate(region_set, 1))
    return tabulate(enumerated_list, headers=['num', 'regions'], tablefmt='grid')

def get_data_by_region(file, region):
    return [row for row in file if row['region'] == region]





