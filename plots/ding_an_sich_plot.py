import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import meros

# Ding an sich graph
# https://stackoverflow.com/questions/8047152/how-do-you-create-a-nested-bar-graph

def ding_an_sich_plot(df, width=1):

    list_columns = df.columns.tolist()
    labels = list(df.groupby(['Label']).groups.keys())
    category_sums = df.groupby(['Category'], as_index=False)[['Amount']].sum()
    category_labels = list(df.groupby(['Category']).groups.keys())
    indices = range(len(df['Category'].unique()))

    plt.bar(indices, category_sums['Amount'].tolist(), width=width,
            color='#D3D3D3', label='Category Sums')

    for ind in indices:
        label = category_labels[ind]
        label_locs = df.loc[df.Category == label].sort_values(by=['Amount'])
        cat_len = len(label_locs)
        locs = subplot_locations(1 / (cat_len * 2), ind, cat_len, width)
        plt.bar(
            locs,
            label_locs['Amount'].tolist(),
            width=(1 / cat_len) * width,
            color=label_locs['Color'].tolist(),
            alpha=0.9
        ) #, label=category_entries['Label'].tolist())

    # plt.bar([i + 0.25 * width for i in indices], lowPower,
    #         width = 0.5 * width, color='r', alpha=0.5, label='Other Power in mW')
    # plt.bar([i - 0.25 * width for i in indices], lowPower2,
    #         width=0.5*width, color='g', alpha=0.5, label='Min Power in mW')
    # plt.bar([i - 0.25 * width for i in indices], lowPower3,
    #         width=0.5 * width, color='g', alpha=0.5, label='Min Power in mW')

    plt.xticks(indices, category_labels)
    plt.legend()
    plt.show()

def subplot_locations(fudge_factor1, index, cat_len, width):
    y = meros.mirror_numbers(cat_len, fudge_factor1, index)
    return [x for x in y]
    # return [i + fudge_factor1 * width for i in range(cat_len)]

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
