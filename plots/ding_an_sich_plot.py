import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

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

# Ding an sich graph
# https://stackoverflow.com/questions/8047152/how-do-you-create-a-nested-bar-graph

def ding_an_sich_plot(df, width=0.9):

    list_columns = df.columns.tolist()
    labels = list(df.groupby(['Label']).groups.keys())
    category_sums = df.groupby(['Category'], as_index=False)[['Amount']].sum()
    category_labels = list(df.groupby(['Category']).groups.keys())
    indices = range(len(df['Category'].unique()))
    xlocs = [i for i in indices]

    plt.bar(indices, category_sums['Amount'].tolist(), width=width,
            color='#D3D3D3', label='Category Sums')

    for i, x in category_sums.iterrows():
        plt.text(xlocs[i] - 0.25, x['Amount'] + 1, x['Category'])

    graph_locs = []
    graph_labs = []

    for ind in indices:
        label = category_labels[ind]
        label_locs = df.loc[df.Category == label].sort_values(by=['Amount'])
        cat_len = len(label_locs)
        locs = subplot_locations(1 / (cat_len * 2), ind, cat_len, width)
        graph_locs.extend(locs)
        graph_labs.extend(label_locs['Label'].tolist())
        plt.bar(
            locs,
            label_locs['Amount'].tolist(),
            width=(1 / cat_len) * width,
            color=label_locs['Color'].tolist(),
            alpha=0.9,
            tick_label=label_locs['Label'].tolist()
        )

    plt.xticks(graph_locs, graph_labs, rotation=90)

    plt.show()

def subplot_locations(fudge_factor, index, cat_len, width):
    y = mirror_numbers_graphing(cat_len, fudge_factor, index, width)
    return [x for x in y]

if __name__ == '__main__':

    data = [
        ['bananas', 'fruits', 10, '#FFE135'],
        ['oranges', 'fruits', 15, '#FFA500'],
        ['tomatoes', 'vegetables', 14, '#FF6347'],
        ['onions', 'vegetables', 11, '#CFB59B'],
        ['cucumbers', 'vegetables', 8, '#284400'],
        ['meat', 'meat', 15, '#000000'],
        ['cod', 'fish', 12, '#008866'],
        ['sole', 'fish', 11, '#D38866'],
        ['tilapia', 'fish', 14, '#008833'],
        ['snapper', 'fish', 13, '#008833'],
        ['chicken', 'eggs', 2, '#557766'],
        ['lizard', 'eggs', 1, '#338866'],
        ['snake', 'eggs', 4, '#003233'],
        ['fish', 'eggs', 3, '#008888'],
        ['platypus', 'eggs', 7, '#001234'],
        ['snapper', 'test', 8, '#008833'],
        ['chicken', 'test', 9, '#557766'],
        ['lizard', 'test', 6, '#338866'],
        ['snake', 'test', 7, '#003233'],
        ['fish', 'test', 8, '#008888'],
        ['platypus', 'test', 8, '#001234'],
        ['octaves', 'test', 8, '#002222'],
        ['plagues', 'test', 8, '#005234']
    ]

    df = pd.DataFrame(data, columns = ['Label', 'Category', 'Amount', 'Color'])
    ding_an_sich_plot(df)
