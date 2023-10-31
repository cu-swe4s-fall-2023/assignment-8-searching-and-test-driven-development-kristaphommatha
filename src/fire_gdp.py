def get_data(file_name, query_column, query_value, header=True):
    result_row = []
    is_on_header = True
    try:
        with open(file_name, 'r') as file:
            for line in file:
                data = line.rstrip().split(',')
                if header is True:
                    if is_on_header is True:
                        result_row.append(data)
                if data[query_column] == str(query_value):
                    result_row.append(data)
                is_on_header = False
    except FileNotFoundError:
        return -1
    except IndexError:
        return -2

    return result_row


def search(nums, key):
    indexes = []
    index = 0
    for k in nums:
        if k == key:
            indexes.append(index)
        index += 1

    return indexes


def get_fire_gdp_year_data():
    pass
