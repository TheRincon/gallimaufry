import matplotlib.pyplot as plt
import pandas as pd
import math
import os
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300
plt.rc_context({'ytick.color':'gray'})

# https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
SMALL_SIZE = 6
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

def mirror_numbers_graphing(n, factor, mid, width):
    # https://stackoverflow.com/questions/38130895/find-middle-of-a-list/38131003
    middle = math.floor(float(n) / 2)
    fudge_array_minus = []
    fudge_array_plus = []
    if n % 2 != 0:
        if middle < 1:
            adj = 1
        else:
            adj = 2
        for i in range(1, middle + 1):
            fudge_array_minus.append(-i * adj * width * factor + mid)
            fudge_array_plus.append(i * adj * factor * width + mid)

        return fudge_array_minus[::-1] + [0.0 + mid] + fudge_array_plus
    else:
        acc = 0
        for i in range(1, middle + 1):
            fudge_array_minus.append((-i - acc) * width * factor + mid)
            fudge_array_plus.append((i + acc) * width * factor + mid)
            acc += 1
        return fudge_array_minus[::-1] + fudge_array_plus

# https://stackoverflow.com/questions/8047152/how-do-you-create-a-nested-bar-graph
def ding_an_sich_plot(df, width=0.9, color='#D3D3D3', xlabel='', ylabel='', title=''):

    list_columns = df.columns.tolist()
    labels = list(df.groupby(['Label']).groups.keys())
    category_sums = df.groupby(['Category'], as_index=False)[['Amount']].sum()
    category_labels = list(df.groupby(['Category']).groups.keys())
    indices = range(len(df['Category'].unique()))
    xlocs = [i for i in indices]

    plt.bar(indices, category_sums['Amount'].tolist(), width=width,
            color=color, label='Category Sums', zorder=50)

    for i, x in category_sums.iterrows():
        plt.text(xlocs[i] - 0.45, x['Amount'] + 5, x['Category'], wrap=True)

    graph_locs = []
    graph_labs = []

    for ind in indices:
        label = category_labels[ind]
        label_locs = df.loc[df.Category == label].sort_values(by=['Amount'], ascending=False)
        cat_len = len(label_locs)
        locs = subplot_locations(1 / (cat_len * 2), ind, cat_len, width)
        graph_locs.extend(locs)
        graph_labs.extend(label_locs['Label'].tolist())
        plt.bar(
            locs,
            label_locs['Amount'].tolist(),
            width=(1 / cat_len) * width,
            color=label_locs['Color'].tolist(),
            alpha=1.0,
            zorder=99,
            tick_label=label_locs['Label'].tolist()
        )

    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=20)
    plt.xticks(graph_locs, graph_labs, rotation=90)
    plt.box(False)
    axes = plt.gca()
    axes.yaxis.grid(alpha=0.5, zorder=0)

    return plt

def subplot_locations(fudge_factor, index, cat_len, width):
    y = mirror_numbers_graphing(cat_len, fudge_factor, index, width)
    return [x for x in y]

def save_figure(fig, output_dir, filename, pad_inches=0.3):
    fig.savefig(os.path.join(output_dir, filename),
                # dpi=fig.dpi,
                bbox_inches='tight',
                pad_inches=pad_inches)
