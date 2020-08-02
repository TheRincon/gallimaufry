import pandas as pd
import matplotlib.pyplot as plt
import os

'''
© 2018 Aaron Penne
Taken from https://github.com/aaronpenne/data_visualization

Assumes the data is already normalized.
'''

def make_output_dir(output_name):
    output_dir = os.path.realpath(output_name)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    return output_dir

def dot_pair_plot(
        df,
        title,
        first_label,
        second_label,
        colors=['#FC8D62', '#65C2A5', '#C947F5'],
        line_color='gray'
    ):
    fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
    for i in df.index:
        x = [df.iloc[i, 0], df.iloc[i, 1]]
        y = [i, i]
        plt.plot(x, y,
                 color=line_color,
                 linestyle='-',
                 linewidth=1)

        if (abs(x[0] - x[1]) < 1.0):
            plt.text(x[0]+4, y[0], df.iloc[i, 2] + ' ({})'.format(df.iloc[i, 0]), horizontalalignment='left', verticalalignment='center', weight='bold')
            plt.text(x[1]-4, y[1], df.iloc[i, 3] + ' ({})'.format(df.iloc[i, 1]), horizontalalignment='right', verticalalignment='center')
            plot_point(plt, df.iloc[i, 0], i, colors[2])
        elif x[0] > x[1]:
            plt.text(x[0]+4, y[0], df.iloc[i, 2] + ' ({})'.format(df.iloc[i, 0]), horizontalalignment='left', verticalalignment='center', weight='bold')
            plt.text(x[1]-4, y[1], df.iloc[i, 3] + ' ({})'.format(df.iloc[i, 1]), horizontalalignment='right', verticalalignment='center')
            plot_point(plt, df.iloc[i, 0], i, colors[0])
            plot_point(plt, df.iloc[i, 1], i, colors[1])
        else:
            plt.text(x[0]-4, y[0], df.iloc[i, 2]  + ' ({})'.format(df.iloc[i, 0]), horizontalalignment='right', verticalalignment='center', weight='bold')
            plt.text(x[1]+4, y[1], df.iloc[i, 3]  + ' ({})'.format(df.iloc[i, 1]), horizontalalignment='left', verticalalignment='center')
            plot_point(plt, df.iloc[i, 0], i, colors[0])
            plot_point(plt, df.iloc[i, 1], i, colors[1])

    for side in ['right', 'left', 'top', 'bottom']:
        ax.spines[side].set_visible(False)

    plt.ylim([-1, 13])
    plt.xlim([-50, 150])
    plt.xticks(range(0,101,10), color='gray')
    plt.yticks([])

    plt.text(-45, 12, title,
             horizontalalignment='left',
             size=16,
             weight='bold')
    plt.text(-45, 11, first_label,
             horizontalalignment='left',
             color=colors[1],
             size=14)
    plt.text(50, 11, second_label,
             horizontalalignment='left',
             color=colors[0],
             size=14)

    return fig

def plot_point(plt, x, index, color):
    plt.plot(x, index,
             color=color,
             linestyle='None',
             marker='o',
             markersize=7,
             fillstyle='full')

def save_figure(fig, output_dir, filename, pad_inches=0.3):
    fig.savefig(os.path.join(output_dir, filename),
                dpi=fig.dpi,
                bbox_inches='tight',
                pad_inches=pad_inches)
