import sys
import matplotlib
matplotlib.use('Agg')  # noqa
import matplotlib.pyplot as plt
import argparse
import fire_gdp


def main():
    try:
        parser = argparse.ArgumentParser(description='Generate fires'
                                                     'and gdp data'
                                                     'for 3 countries',
                                         prog='fire_gdp')

        parser.add_argument('--ff',
                            type=str,
                            help='Name of fires data file',
                            required=True)

        parser.add_argument('--gf',
                            type=str,
                            help='Name of gdp data file',
                            required=True)

        parser.add_argument('--c1',
                            type=str,
                            help='Name of first country',
                            required=True)

        parser.add_argument('--c2',
                            type=str,
                            help='Name of second country',
                            required=True)

        parser.add_argument('--c3',
                            type=str,
                            help='Name of third country',
                            required=True)

        parser.add_argument('--q',
                            type=int,
                            help='Index of column in fires file'
                                 'to collect data from',
                            required=True)

        parser.add_argument('--y',
                            type=int,
                            help='Index of column in fires file'
                                 'that contains year data',
                            nargs='?',
                            const=1,
                            default=1)

        args = parser.parse_args()

    except Exception as e:
        print('Invalid input')
        sys.exit(1)

    c1_datas = fire_gdp.get_fire_gdp_year_data(args.ff, args.gf,
                                               args.c1, args.q,
                                               args.y)
    c2_datas = fire_gdp.get_fire_gdp_year_data(args.ff, args.gf,
                                               args.c2, args.q,
                                               args.y)
    c3_datas = fire_gdp.get_fire_gdp_year_data(args.ff, args.gf,
                                               args.c3, args.q,
                                               args.y)
    if (c1_datas == -3 or c2_datas == -3 or c3_datas == -3):
        print('Could not find information on country in fires file'
              ' or gdp file')
        sys.exit()

    if (type(c1_datas) == int or type(c2_datas) == int or
            type(c3_datas) == int):
        print('An error occurred.')
        sys.exit(1)

    result1 = fire_gdp.write_to_file('../data/' + args.c1 + '.csv', c1_datas)
    result2 = fire_gdp.write_to_file('../data/' + args.c2 + '.csv', c2_datas)
    result3 = fire_gdp.write_to_file('../data/' + args.c3 + '.csv', c3_datas)


if __name__ == '__main__':
    main()
