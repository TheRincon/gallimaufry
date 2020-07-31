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

def make_new_df(df):
    col_list = df.columns.tolist()
    df2 = pd.DataFrame(columns = col_list)
    df2['original_index'] = None
    return df2

def dot_pair_plot(
        df,
        title,
        first_label,
        second_label,
        colors=['#FC8D62', '#65C2A5', '#C947F5'],
        line_color='gray'
    ):

    df2 = make_new_df(df)
    fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
    for i in df.index:
        print(df.iloc[i, 0])
        x = [df.iloc[i, 0], df.iloc[i, 1]]
        y = [i, i]
        plt.plot(x, y,
                 color=line_color,
                 linestyle='-',
                 linewidth=1)

        if (abs(x[0] - x[1]) < 1.0):
            plt.text(x[0]+4, y[0], df.iloc[i, 2] + ' ({})'.format(df.iloc[i, 0]), horizontalalignment='left', verticalalignment='center', weight='bold')
            plt.text(x[1]-4, y[1], df.iloc[i, 3] + ' ({})'.format(df.iloc[i, 1]), horizontalalignment='right', verticalalignment='center')
            df2.loc[df.index[i]] = df.iloc[i]
            df2.loc[df.index[i], 'original_index'] = i
            df = df.drop(df.index[[i]])
            # Index is messed up because it's still looping over df.index
            # df.reset_index(drop=True, inplace=True)
            # Move this out of the loop, pre-process it.
        elif x[0] > x[1]:
            plt.text(x[0]+4, y[0], df.iloc[i, 2] + ' ({})'.format(df.iloc[i, 0]), horizontalalignment='left', verticalalignment='center', weight='bold')
            plt.text(x[1]-4, y[1], df.iloc[i, 3] + ' ({})'.format(df.iloc[i, 1]), horizontalalignment='right', verticalalignment='center')
        else:
            plt.text(x[0]-4, y[0], df.iloc[i, 2]  + ' ({})'.format(df.iloc[i, 0]), horizontalalignment='right', verticalalignment='center', weight='bold')
            plt.text(x[1]+4, y[1], df.iloc[i, 3]  + ' ({})'.format(df.iloc[i, 1]), horizontalalignment='left', verticalalignment='center')

    if len(df2.index) != 0:
        x = df2.iloc[:, 0]
        y = df2['original_index']
        plt.plot(x, y,
                 color=colors[2],
                 linestyle='None',
                 marker='o',
                 markersize=7,
                 fillstyle='full')

    x = df.iloc[:, 1]
    y = df.index
    plt.plot(x, y,
             color=colors[0],
             linestyle='None',
             marker='o',
             markersize=7,
             fillstyle='full')

    x = df.iloc[:, 0]
    y = df.index
    plt.plot(x, y,
             color=colors[1],
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

    plt.text(-45, 12, title,
             horizontalalignment='left',
             size=16,
             weight='bold')
    plt.text(-45, 11, first_label,
             horizontalalignment='left',
             color=colors[0],
             size=14)
    plt.text(60, 11, second_label,
             horizontalalignment='left',
             color=colors[1],
             size=14)

    return fig

def save_figure(fig, output_dir, filename, pad_inches=0.3):
    fig.savefig(os.path.join(output_dir, filename),
                dpi=fig.dpi,
                bbox_inches='tight',
                pad_inches=pad_inches)

if __name__ == '__main__':
    # Example:
    # https://aflcio.org/paywatch/highest-paid-ceos
    # https://aflcio.org/paywatch/company-pay-ratios
    df = pd.read_csv('/home/rincon/Desktop/data.csv', header=None)
    output_dir = make_output_dir('/home/rincon/Desktop/data_dir')
    fig = dot_pair_plot(df,
      'Annual CEO Compensation and Median Worker Pay',
      'CEO pay in millions $',
      'Worker pay in thousands $'
    )
    save_figure(fig, output_dir, 'test.png', colors=['#FF00FF', '#40E0D0', '#FFDF00 '])
