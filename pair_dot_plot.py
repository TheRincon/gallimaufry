import pandas as pd
import matplotlib.pyplot as plt
import os

'''
© 2018 Aaron Penne
Taken from https://github.com/aaronpenne/data_visualization

Adapted for general normalized quantity use.
'''

def make_output_dir(output_name):
    output_dir = os.path.realpath(output_name)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

# a_compensation = 0
# a_revenue = 1
# ceo = 2
# comapny = 3

def make_new_df(df):
    col_list = df.columns.tolist()
    df2 = pd.DataFrame(columns = col_list)
    df2['original_index'] = None
    return df2

def dot_pair_plot(df):
    df2 = make_new_df(df)
    fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
    for i in df.index:
        x = [df.iloc[i, 0], df.iloc[i, 1]]
        y = [i, i]
        plt.plot(x, y,
                 color='gray',
                 linestyle='-',
                 linewidth=1)

        if (abs(x[0] - x[1]) < 1.0):
            plt.text(x[0]+4, y[0], df.iloc[i, 2], horizontalalignment='left', verticalalignment='center', weight='bold')
            plt.text(x[1]-4, y[1], df.iloc[i, 3], horizontalalignment='right', verticalalignment='center')
            df2.loc[df.index[i]] = df.iloc[i]
            df2.loc[df.index[i], 'original_index'] = i
            df = df.drop(df.index[[i]])
        elif x[0] > x[1]:
            plt.text(x[0]+4, y[0], df.iloc[i, 2], horizontalalignment='left', verticalalignment='center', weight='bold')
            plt.text(x[1]-4, y[1], df.iloc[i, 3], horizontalalignment='right', verticalalignment='center')
        else:
            plt.text(x[0]-4, y[0], df.iloc[i, 2], horizontalalignment='right', verticalalignment='center', weight='bold')
            plt.text(x[1]+4, y[1], df.iloc[i, 3], horizontalalignment='left', verticalalignment='center')
    if len(df2.index) != 0:
        x = df2.iloc[:, 0]
        y = df2['original_index']
        plt.plot(x, y,
                 color='#C947F5',
                 linestyle='None',
                 marker='o',
                 markersize=7,
                 fillstyle='full')

    # Plot revenue
    x = df.iloc[:, 0]
    y = df.index
    # #C947F5
    plt.plot(x, y,
             color='#65C2A5',
             linestyle='None',
             marker='o',
             markersize=7,
             fillstyle='full')

    # Plot company
    x = df.iloc[:, 1]
    y = df.index
    plt.plot(x, y,
             color='#FC8D62',
             linestyle='None',
             marker='o',
             markersize=7,
             fillstyle='full')

    for side in ['right', 'left', 'top', 'bottom']:
        ax.spines[side].set_visible(False)

    plt.ylim([-1, 13])
    plt.xlim([-50, 150])
    plt.xticks(range(0,101,10), color='gray')
    ax.set_yticklabels('')

    plt.text(-45, 12, 'Annual Company Revenue and Annual CEO Compensation',
             horizontalalignment='left',
             size=16,
             weight='bold')
    plt.text(-45, 11, 'Company revenue is in $Billions.',
             horizontalalignment='left',
             color='#FC8D62',
             size=14)
    plt.text(60, 11, 'CEO compensation is in $Millions.',
             horizontalalignment='left',
             color='#65C2A5',
             size=14)
    plt.text(-50, -3, 'Example text',
             horizontalalignment='left',
             color='gray',
             size=8)

    return fig

def save_figure(fig, output_dir, filename, pad_inches=0.3):
    fig.savefig(os.path.join(output_dir, filename),
                dpi=fig.dpi,
                bbox_inches='tight',
                pad_inches=pad_inches)

if __name__ == '__main__':
    df = pd.read_csv('/home/rincon/Desktop/data.csv', header=None)
    make_output_dir('/home/rincon/Desktop/data_dir')
    fig = dot_pair_plot(df)
    save_figure(fig, '/home/rincon/Desktop/data_dir', 'testerrr.png') # save_figure(fig, output_name, figname)