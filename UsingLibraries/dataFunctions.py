import panda as pd
import matplotlib as plt


def collect_fire_years_data(file_name, query_col, query_value, target_stats):
    try:
        total_df = pd.read_csv(file_name)
    except FileNotFoundError:
        return -1
    except Exception as e:
        return None
    target_stats.insert(0, 'Year')
    query_df = total_df[total_df[query_col] == query_value]
    target_df = query_df[target_stats]
    return target_df


def destroy_commas(x):  # function to remove commas from column values and turn to floats
    if x is not np.nan:
        return float(x.replace(',', ''))
    else:
        return x


def clean_data(file_name):
    try:
        total_df = pd.read_csv(file_name)
    except FileNotFoundError:
        return -1
    except Exception as e:
        return None

    total_df.replace('...', None, inplace=True)
    total_df.replace('-', None, inplace=True)
    for col in total_df.columns:
        if col == 'Country':
            continue
        total_df[col] = total_df[col].apply(destroy_commas)
    return 0
