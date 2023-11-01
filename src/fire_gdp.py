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


def get_fire_gdp_year_data():
    pass
