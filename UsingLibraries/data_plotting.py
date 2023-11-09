import matplotlib.pyplot as plt
import pandas as pd
import dataFunctions as dfs
import sys


def main():
    fire_file = '../data/Agrofood_co2_emission.csv'
    gdp_file = '../data/CLEAN_IMF_GDP.csv'
    target_stats = ['Average Temperature °C', 'total_emission',
                    'Urban population']

    US_df = dfs.get_fire_gdp_year_data(fire_file, gdp_file,
                                       'United States of America',
                                       target_stats)
    Mexico_df = dfs.get_fire_gdp_year_data(fire_file, gdp_file,
                                           'Mexico', target_stats)
    Canada_df = dfs.get_fire_gdp_year_data(fire_file, gdp_file,
                                           'Canada', target_stats)
    Guat_df = dfs.get_fire_gdp_year_data(fire_file, gdp_file,
                                         'Guatemala', target_stats)

    fig, axes = plt.subplots(2, 2, height_ratios=[1, 1.5])
    fig.set_size_inches(13, 10)
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
        print('An error as occured in figure A')

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
        print('An error as occured in figure B')

    axes[0, 1].set_xlabel('Year')
    axes[0, 1].set_ylabel('Total Emissions')
    axes[0, 1].legend(loc='upper left')
    axes[0, 1].set_title('B', loc='left')
    axes[0, 1].spines[['right', 'top']].set_visible(False)

    cmin1, cmax1 = dfs.find_total_range(US_df, Mexico_df, Canada_df, Guat_df,
                                        'Year')
    try:
        sc1 = axes[1, 0].scatter(US_df['GDP'], US_df['total_emission'],
                                 c=US_df['Year'], vmin=cmin1, vmax=cmax1,
                                 cmap='summer', label='United States',
                                 marker='d', alpha=.75)
        sc2 = axes[1, 0].scatter(Mexico_df['GDP'], Mexico_df['total_emission'],
                                 c=Mexico_df['Year'], vmin=cmin1, vmax=cmax1,
                                 cmap='summer', label='Mexico',
                                 marker='s', alpha=.75)
        sc3 = axes[1, 0].scatter(Canada_df['GDP'], Canada_df['total_emission'],
                                 c=Canada_df['Year'], vmin=cmin1, vmax=cmax1,
                                 cmap='summer', label='Canada',
                                 marker='o', alpha=.75)
        sc4 = axes[1, 0].scatter(Guat_df['GDP'], Guat_df['total_emission'],
                                 c=Guat_df['Year'], vmin=cmin1, vmax=cmax1,
                                 cmap='summer', label='Guatemala',
                                 marker='^', alpha=.75)
    except Exception as e:
        print('An error as occured in figure C')

    axes[1, 0].set_xlabel('GDP')
    axes[1, 0].set_ylabel('Total Emissions')
    axes[1, 0].legend(loc='upper left')
    axes[1, 0].set_title('C', loc='left')
    axes[1, 0].spines[['right', 'top']].set_visible(False)
    fig.colorbar(sc1, label='Year', ax=axes[1, 0], orientation="horizontal")

    cmin2, cmax2 = dfs.find_total_range(US_df, Mexico_df, Canada_df, Guat_df,
                                        'total_emission')
    try:
        sc1 = axes[1, 1].scatter(US_df['Urban population'],
                                 US_df['GDP'],
                                 c=US_df['total_emission'],
                                 vmin=cmin2, vmax=cmax2,
                                 cmap='spring', label='United States',
                                 marker='d', alpha=.75)
        sc2 = axes[1, 1].scatter(Mexico_df['Urban population'],
                                 Mexico_df['GDP'],
                                 c=Mexico_df['total_emission'],
                                 vmin=cmin2, vmax=cmax2,
                                 cmap='spring', label='Mexico',
                                 marker='s', alpha=.75)
        sc3 = axes[1, 1].scatter(Canada_df['Urban population'],
                                 Canada_df['GDP'],
                                 c=Canada_df['total_emission'],
                                 vmin=cmin2, vmax=cmax2,
                                 cmap='spring', label='Canada',
                                 marker='o', alpha=.75)
        sc4 = axes[1, 1].scatter(Guat_df['Urban population'],
                                 Guat_df['GDP'],
                                 c=Guat_df['total_emission'],
                                 vmin=cmin2, vmax=cmax2,
                                 cmap='spring', label='Guatemala',
                                 marker='^', alpha=.75)
    except Exception as e:
        print('An error as occured in figure D')

    axes[1, 1].set_xlabel('Urban population')
    axes[1, 1].set_ylabel('GDP')
    axes[1, 1].legend(loc='upper left')
    axes[1, 1].set_title('D', loc='left')
    axes[1, 1].spines[['right', 'top']].set_visible(False)
    fig.colorbar(sc1, label='Total Emissions', ax=axes[1, 1],
                 orientation="horizontal")

    plt.savefig('../data/Homework9.png', dpi=300)


if __name__ == "__main__":
    main()
