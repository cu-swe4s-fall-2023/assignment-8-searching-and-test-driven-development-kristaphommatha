import plt as matplotlib
import pandas as pd
import dataFunctions as dfs


def main():
    fire_file = '../data/Agrofood_co2_emission.csv'
    target_stats = ['Average Temperature °C', 'total_emission']

    US_df = dfs.collect_fire_years_data(fire_file, 'Area',
                                        'United States of America',
                                        target_stats)
    Mexico_df = dfs.collect_fire_years_data(fire_file, 'Area',
                                            'Mexico', target_stats)
    Canada_df = dfs.collect_fire_years_data(fire_file, 'Area',
                                            'Canada', target_stats)
    Guat_df = dfs.collect_fire_years_data(fire_file, 'Area',
                                          'Guatemala', target_stats)

    fig, axes = plt.subplots(2, 2)
    fig.set_size_inches(10, 10)
    axes[0, 0].plot(US_df['Year'], US_df['Average Temperature °C'],
                    label='United States')
    axes[0, 0].plot(Mexico_df['Year'], Mexico_df['Average Temperature °C'],
                    label='Mexico')
    axes[0, 0].plot(Canada_df['Year'], Canada_df['Average Temperature °C'],
                    label='Canada')
    axes[0, 0].plot(Guat_df['Year'], Guat_df['Average Temperature °C'],
                    label='Guatemala')
    axes[0, 0].set_xlabel('Year')
    axes[0, 0].set_ylabel('Average Temperature °C')
    axes[0, 0].legend(loc='upper left')
    axes[0, 0].set_title('A', loc='left')
    axes[0, 0].spines[['right', 'top']].set_visible(False)

    axes[0, 1].scatter(US_df['Year'], US_df['total_emission'],
                       label='United States', alpha=.75)
    axes[0, 1].scatter(Mexico_df['Year'], Mexico_df['total_emission'],
                       label='Mexico', alpha=.75)
    axes[0, 1].scatter(Canada_df['Year'], Canada_df['total_emission'],
                       label='Canada', alpha=.75)
    axes[0, 1].scatter(Guat_df['Year'], Guat_df['total_emission'],
                       label='Guatemala', alpha=.75)
    axes[0, 1].set_xlabel('Year')
    axes[0, 1].set_ylabel('Total Emissions')
    axes[0, 1].legend(loc='upper left')
    axes[0, 1].set_title('B', loc='left')
    axes[0, 1].spines[['right', 'top']].set_visible(False)


if __name__ == "__main__":
    main()
