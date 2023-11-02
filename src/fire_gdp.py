def get_data(file_name, query_column, query_value, header=True):
    result_row = []
    is_on_header = True
    try:
        with open(file_name, 'r') as file:
            for line in file:
                data = splitter(line.rstrip(), '"', ',')
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
    except Exception as e:
        return -3

    return result_row


def search(nums, key):
    indexes = []
    index = 0
    for k in nums:
        if k == key:
            indexes.append(index)
        index += 1
    if len(indexes) == 0:
        return None
    return indexes


def splitter(string, delimiter1, delimiter2):
    new_strings = []
    delim2_start_index = -1
    # flag to indicate that we are in between two delimiter1s
    delim1_bool = False
    char_counter = 0
    for char in string:
        # 1st quotation was found
        if (char == delimiter1 and delim1_bool is False):
            delim1_bool = True
            delim1_start_index = char_counter  # save location of 1st delim1

        # 2nd quotation was found
        elif (char == delimiter1 and delim1_bool is True):
            new = string[delim1_start_index + 1:char_counter]
            new_strings.append(new)
            delim1_bool = False
            delim2_start_index = char_counter + 1

        # Internal comma was found
        if (char == delimiter2 and delim1_bool is True):
            pass

        # External comma was found
        if (char == delimiter2 and delim1_bool is False):
            # catch that no empty strings are made
            if delim2_start_index != char_counter:
                new = string[delim2_start_index + 1:char_counter]
                delim2_start_index = char_counter  # Update location of delim2
                new_strings.append(new)
        if char_counter == len(string) - 1:  # at the end of the string
            if char != '"':
                new = string[delim2_start_index + 1:char_counter + 1]
                new_strings.append(new)
        char_counter += 1

    return new_strings


def string_with_comma_to_float(string):
    if len(string) != 0:
        new_string = string.replace(',','')
        return float(new_string)
    else:
        return None


def get_fire_gdp_year_data(fires_file, gdp_file,
                           target_country, target_column, year_col):
# fires_file = file name containing CO2 data
# gdp_file = file name containing GDP data
# target_country = country to find info on
# query_columns = list of columns to generate data on

#(file_name, query_column, query_value, header=True)
    fires = []
    gdps = []
    years = []
    
    fire_data = get_data(fires_file, 0, target_country, header=False)
    gdp_data = get_data(gdp_file, 0, target_country)

    # catch error in get_data
    if(type(fire_data) == int or type(gdp_data) ==  int):
        return -1  # exit code for bad file inputs
    else:  # get data worked
        if (len(fire_data) == 0 or len(gdp_data) <= 1):
            return -3 # exit code for country or year could not be found
        if year_col >= len(fire_data):
            return -2 # exit code for range error in target column or year col

        for row in fire_data:  # search every row including info about the country
            current_year = row[year_col]  # grab the associated year
            year_indexes = search(gdp_data[0], current_year)  # find gdp data from current year
            if year_indexes is not None:
                for index in year_indexes:  # for all occurences of year in gdp_data
                    if target_column < len(row):  # check if target_column is in range
                        # check if gdp data is not empty
                        if (gdp_data[1][index] != '...' and gdp_data[1][index] != '-'):
                            fires.append(float(row[target_column]))
                            gdps.append(string_with_comma_to_float(gdp_data[1][index]))
                            years.append(int(current_year))
                    else:  # exit code for range error in target column or year col
                        return -2
        if len(years) == 0:
            return -3

        return fires, gdps, years
    