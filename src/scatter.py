import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')  # noqa
import matplotlib.pyplot as plt
import argparse


def make_scatter(data_file, out_file, title, x, y):
    try:
        for line in open(data_file):
            A = line.rstrip().split(',')
            X.append(float(A[0]))
            Y.append(float(A[1]))
    except Exception as e:
        return -1

    fig, ax = plt.subplots()
    ax.scatter(X, Y)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(title)

    plt.savefig(out_file, bbox_inches='tight')


def main():
    try:
        parser = argparse.ArgumentParser(description='Call scatter function'
                                                     'to make scatter plot',
                                         prog='make_scatter')

        parser.add_argument('--df',
                            type=str,
                            help='Name of data file to enter',
                            required=True)

        parser.add_argument('--of',
                            type=str,
                            help='Name of file to output',
                            required=True)

        parser.add_argument('--t',
                            type=str,
                            help='Title of scatter plot',
                            required=True)

        parser.add_argument('--x',
                            type=str,
                            help='x-axis label',
                            required=True)

        parser.add_argument('--y',
                            type=str,
                            help='y-axis label',
                            required=True)

        args = parser.parse_args()

    except Exception as e:
        print('Invalid input')
        sys.exit(1)

    scatterplot = make_scatter(args.df, args.of, args.t, args.x, args.y)
    if scatter_plot == -1:
        sys.exit(1)


if __name__ == '__main__':
    main()
