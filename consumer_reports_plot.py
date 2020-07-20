import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import seaborn as sns; sns.set() # comment this out for borders on plot

plt.rcParams["axes.grid"] = False

'''
Preferred aspect ration is 0.15
Use larger width if more space is needed (text is constant dimensions, more or less)
'''

def cr_plot(data, row_labels, column_labels, output_path, default_val=0, width=15, colormap=None, graph_aspect=0.15, set_max=False, title=None):
    if len(row_labels) < 2:
        raise ValueError('Number of subplots must be greater than 1, just make plot manually')

    figw = width
    figh = figw * graph_aspect

    data = np.nan_to_num(data, nan=default_val) # comment out for gray spots on graph for NAN
    colormap = 'Wistia' if colormap is None else colormap # find out how to pass in colormap
    cmap = plt.cm.get_cmap(colormap, len(column_labels))
    norm = matplotlib.colors.Normalize(vmin= data.min(), vmax= data.max()) # add option to use global max or row max
    bound = np.linspace(0, 1, len(column_labels))
    bound_prep = np.round(bound * data.max())
    gridspec_kw = {"height_ratios": [1] * len(row_labels), "width_ratios" : [1]}
    fig, axes = plt.subplots(ncols=1, nrows=len(row_labels), figsize=(figw, figh), gridspec_kw=gridspec_kw, sharex=True)

    for i, ax in enumerate(axes):
        dat = np.asarray(data[i,:]).reshape(1, data.shape[1])
        im = ax.imshow(dat, cmap=colormap, aspect=0.3, norm=norm)
        # https://stackoverflow.com/a/26094524
        ax.plot([-0.21, 1], [-0.5, -0.5], color='black', lw=1, transform=ax.transAxes, clip_on=False)
        ax.plot([-0.21, 1], [1.5, 1.5], color='black', lw=1, transform=ax.transAxes, clip_on=False)
        ax.xaxis.set_visible(False) # fix this, need the x-axis values
        ax.set_ylabel(row_labels[i], rotation=0)
        first, second = yaxis_coords(len(row_labels))
        ax.yaxis.set_label_coords(first, second)
        ax.set_yticks([])

    plt.subplots_adjust(hspace=1)
    plt.legend([mpatches.Patch(color=cmap(b)) for b in bound[:-1]],
           ['{} - {}'.format(int(bound_prep[i]), int(bound_prep[i+1])) for i in range(len(column_labels))],
           loc= (1.1, 1), title=r"$\bf{" + title + "}$")
    plt.savefig(output_path)

def yaxis_coords(number_of_subplots):
    first = -0.07 - (0.01 * number_of_subplots)
    second = 0.55 - (0.1 * number_of_subplots)
    return (first, second)

if __name__ == "__main__":
    cars = ['Toyota Corrola', 'Toyota Camry', 'Toyota Prius']
    years = [2015, 2016, 2017, 2018, 2019, 2020]
    samps = np.array([[0, 0, 0, 5000, 7000, 10000],
                    [0, 0, 5000, 7000, 9000, 12000],
                    [7000, 9000, 11000, 13000, 15000, 16000]]
                )
    output_path = 'car_tester.png'
    cr_plot(samps, cars, years, output_path, colormap= 'viridis',title='Used \ car \ price') # \ needed for spaces in math mode!