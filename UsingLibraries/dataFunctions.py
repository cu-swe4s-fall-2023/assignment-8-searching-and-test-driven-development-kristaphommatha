import pandas as pd


def collect_fire_years_data(file_name, country_col, country, target_stats):
    try:
        total_df = pd.read_csv(file_name)
    except FileNotFoundError:
        return -1
    except Exception as e:
        return 0
    target_and_year = ['Year'] + target_stats
    query_df = total_df[total_df[country_col].str.contains(country)]
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
    total_df.replace('United States', 'United States of America',
                     inplace=True)
    for col in total_df.columns:
        if col == 'Country':
            continue
        total_df[col] = total_df[col].apply(destroy_commas)
        total_df.to_csv('CLEAN_' + file_name, sep=',', index=False)
    return 0


def get_fire_gdp_year_data(fires_file, gdp_file, country, target_stats):
    try:
        gdp_df = pd.read_csv(gdp_file)
    except FileNotFoundError:
        return -1
    except Exception as e:
        return None

    country_fires_df = collect_fire_years_data(fires_file, 'Area',
                                               country, target_stats)

    country_gdp_df = gdp_df[gdp_df['Country'] == country]
    country_gdp_df = country_gdp_df.T.reset_index()
    country_gdp_df.columns = ['year', 'GDP']
    country_gdp_df = country_gdp_df.iloc[1:, :]
    country_gdp_df['year'] = country_gdp_df['year'].astype('int64')
    # print(country_gdp_df)
    try:
        country_df = pd.merge(country_fires_df, country_gdp_df,
                              how='inner', left_on='Year',
                              right_on='year')
    except Exception as e:
        return -1

    country_df = country_df.drop('year', axis=1)
    return country_df


def find_total_range(df1, df2, df3, df4, target_stat):
    df_mins = []
    df_maxs = []

    df_mins.append(df1[target_stat].min())
    df_mins.append(df2[target_stat].min())
    df_mins.append(df3[target_stat].min())
    df_mins.append(df4[target_stat].min())

    df_maxs.append(df1[target_stat].max())
    df_maxs.append(df2[target_stat].max())
    df_maxs.append(df3[target_stat].max())
    df_maxs.append(df4[target_stat].max())

    return min(df_mins), max(df_maxs)
