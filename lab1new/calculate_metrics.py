import statistics as st
import numpy as np
import math
from tabulate import tabulate
from error_messages import *
from output_data import *

metrics = {'max_value':"0", 'min_value':"0", 'mean_value':"0", 'median_value':"0"}

def get_metrics(column_metrics):
    metrics['max_value'] = max(column_metrics)
    metrics['min_value'] = min(column_metrics)
    metrics['mean_value'] = st.mean(column_metrics)
    metrics['median_value'] = st.median(column_metrics)
    return metrics

def calculate_perceniles(data):
    percentiles_array = []
    for i in range(0, 101, 5):
        percentile_value = np.percentile(data, i)
        percentiles_array.append([f'{i}%', percentile_value])
    return tabulate(percentiles_array, headers=['%', 'value'], tablefmt='grid')

def show_metrics_by_needed_column(file, column_num):
    column_num -= 1
    column_keys = list(file[0].keys())
    column_value = column_keys[column_num]
    column_metrics = []
    flag = False
    for row in file:
        cell_value = row[column_value].replace(' ', '')
        if cell_value == '':
            continue
        if cell_value.isalpha():
            flag = True
            break
        column_metrics.append(cell_value)
    if flag == True or len(column_metrics) == 0:
        output_value_of_column_error()
        return

    column_metrics = [float(x) for x in column_metrics]
    #print(column_metrics)

    metric_dict = (get_metrics(column_metrics))
    print_metrics(metric_dict['max_value'], metric_dict['min_value'], metric_dict['mean_value'], metric_dict['median_value'])
    data = sorted(column_metrics)
    percentiles = calculate_perceniles(data)
    print_percentile_table(percentiles)


