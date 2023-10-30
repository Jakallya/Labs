from calculate_metrics import *
from work_with_table import *
from error_messages import *
from input_data import *
from output_data import *

def start():
    file_path = input_file()
    file_check_result = check_file_path(file_path)
    if check_file_path(file_path):
        show_error_messages(file_check_result)
        return

    #csvfile = open(file_path, mode='r')
    with open(file_path, mode='r') as csvfile:
        file = get_data_from_table(csvfile)

    if not check_regions(file):
        show_error_messages(EMPTY_REGIONS_ERROR)
        return

    region_base = get_regions(file)
    print_regions(region_base)

    region = input_region()

    region_data = get_data_by_region(file, region)
    if not region_data:
        show_error_messages(INPUT_REGION_ERROR)
        return

    print_table(region_data)

    column_num = input_column_id()
    if check_num_column(column_num, file):
        show_error_messages(ID_COLUMN_ERROR)
        return

    show_metrics_by_needed_column(region_data, column_num)



