def get_data(file_name, query_column, query_value, header = True):
    result_row = []
    header = []
    is_on_header = True
    try:
        with open(file_name, 'r') as file:
            for line in file:
                data = line.rstrip().split(',')
                if header == True and is_on_header:
                    header = data
                if data[query_column] == str(query_value):
                    result_row.append(data)
                is_on_header = False
    except FileNotFoundError:
        return -1
    except IndexError:
        return -2

    if header == False:
        return result_row
    if header == True:
        return result_row, header

def search():
    pass
    
def get_fire_gdp_year_data():
    pass
