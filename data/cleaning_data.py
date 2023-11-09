import sys
sys.path.insert(0, '../UsingLibraries')  # noqa
import dataFunctions as dfs
import argparse


def main():
    try:
        parser = argparse.ArgumentParser(description='Clean data file',
                                         prog='dataFunctions.py')

        parser.add_argument('--f',
                            type=str,
                            help='Name of data file to clean',
                            required=True)
        args = parser.parse_args()

    except Exception as e:
        sys.exit(1)

    dfs.clean_data(args.f)
    print('Cleanup completed')


if __name__ == "__main__":
    main()
