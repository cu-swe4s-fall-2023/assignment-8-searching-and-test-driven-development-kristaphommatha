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

    if country_fires_df != -1 or country_fires_df != 0:
        country_gdp_df = gdp_df[gdp_df['Country'] == country]
        country_gdp_df = country_gdp.df.T.reset_index()
        country_gdp_df = ['year', 'GDP']
        country_gdp_df = country_gdp_df.iloc[1:, :]
        country_gdp_df['year'] = country_gdp_df['year'].astype('int64')

        country_df = pd.merge(country_fire_df, country_gdp_df,
                              how='inner', left_on='Year',
                              right_on='year')
        country_df = country_df.drop('year', axis=1)
        return country_df
    else:
        return -1
