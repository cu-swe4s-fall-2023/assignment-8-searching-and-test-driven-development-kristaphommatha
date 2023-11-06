import pandas as pd


def collect_fire_years_data(file_name, query_col, query_value, target_stats):
    try:
        total_df = pd.read_csv(file_name)
    except FileNotFoundError:
        return -1
    except Exception as e:
        return None
    target_and_year = ['Year'] + target_stats
    query_df = total_df[total_df[query_col] == query_value]
    target_df = query_df[target_and_year]
    return target_df


def destroy_commas(x):
    if x is not None:
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
        total_df.to_csv('CLEAN_' + file_name, sep=',', index=False)
    return 0
