import plt as matplotlib
import pandas as pd
import dataFunctions as dfs
import sys


def main():
    fire_file = '../data/Agrofood_co2_emission.csv'
    gdp_file = '../data/CLEAN_IMF_GDP.csv'
    target_stats = ['Average Temperature °C', 'total_emission']

    US_df = dfs.get_fire_gdp_year_data(fire_file, gdp_file,
                                       'United States of America',
                                       target_stats)
    Mexico_df = dfs.get_fire_gdp_year_data(fire_file, gdp_file,
                                           'Mexico', target_stats)
    Canada_df = dfs.get_fire_gdp_year_data(fire_file, gdp_file,
                                           'Canada', target_stats)
    Guat_df = dfs.get_fire_gdp_year_data(fire_file, gdp_file,
                                         'Guatemala', target_stats)

    fig, axes = plt.subplots(2, 2)
    fig.set_size_inches(10, 10)
    try:
        axes[0, 0].plot(US_df['Year'], US_df['Average Temperature °C'],
                        label='United States')
        axes[0, 0].plot(Mexico_df['Year'], Mexico_df['Average Temperature °C'],
                        label='Mexico')
        axes[0, 0].plot(Canada_df['Year'], Canada_df['Average Temperature °C'],
                        label='Canada')
        axes[0, 0].plot(Guat_df['Year'], Guat_df['Average Temperature °C'],
                        label='Guatemala')
    except Exception as e:
        print('An error occured.')

    axes[0, 0].set_xlabel('Year')
    axes[0, 0].set_ylabel('Average Temperature °C')
    axes[0, 0].legend(loc='upper left')
    axes[0, 0].set_title('A', loc='left')
    axes[0, 0].spines[['right', 'top']].set_visible(False)

    try:
        axes[0, 1].scatter(US_df['Year'], US_df['total_emission'],
                           label='United States', alpha=.75)
        axes[0, 1].scatter(Mexico_df['Year'], Mexico_df['total_emission'],
                           label='Mexico', alpha=.75)
        axes[0, 1].scatter(Canada_df['Year'], Canada_df['total_emission'],
                           label='Canada', alpha=.75)
        axes[0, 1].scatter(Guat_df['Year'], Guat_df['total_emission'],
                           label='Guatemala', alpha=.75)
    except Exception as e:
        print('An error occured.')

    axes[0, 1].set_xlabel('Year')
    axes[0, 1].set_ylabel('Total Emissions')
    axes[0, 1].legend(loc='upper left')
    axes[0, 1].set_title('B', loc='left')
    axes[0, 1].spines[['right', 'top']].set_visible(False)
    
    try:
        sc1 = axes[1, 0].scatter(US_df['GDP'], US_df['total_emission'],
                                 c=US_df['Year'], label='United States',
                                 marker='d', alpha=.75)
        sc2 = axes[1, 0].scatter(Mexico_df['GDP'], Mexico_df['total_emission'],
                                 c=Mexico_df['Year'], label='Mexico',
                                 marker='s', alpha=.75)
        sc3 = axes[1, 0].scatter(Canada_df['GDP'], Canada_df['total_emission'],
                                 c=Canada_df['Year'], label='Canada',
                                 marker='o', alpha=.75)
        sc4 = axes[1, 0].scatter(Guat_df['GDP'], Guat_df['total_emission'],
                                 c=US_df['Year'], label='Guatemala',
                                 marker='P', alpha=.75)
    except Exception as e:
        print('An error occured.')

    axes[1, 0].set_xlabel('GDP')
    axes[1, 0].set_ylabel('Total Emissions')
    axes[1, 0].legend(loc='upper left')
    axes[1, 0].set_title('C', loc='left')
    axes[1, 0].spines[['right', 'top']].set_visible(False)
    fig.colorbar(sc1,label='Year',ax=axes[1,0], orientation="horizontal")


if __name__ == "__main__":
    main()
