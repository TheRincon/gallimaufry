import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams["axes.grid"] = False

'''
Preferred aspect ration is 0.15
Use larger width if more space is needed (text is constant dimensions, more or less)

 '\' is needed in the title string for spaces in math mode!
'''

def bound_creation(data, column_labels):
    bound = np.linspace(0, 1, len(column_labels) + 1)
    bound_prep = np.round(bound * data.max())

    return bound, bound_prep

def get_colors(inp, colormap, vmin=None, vmax=None):
    norm = plt.Normalize(vmin, vmax)
    return colormap(norm(inp))

def legend_data(cmap, bound, bound_prep, column_labels):
    patches = [mpatches.Patch(color=cmap(b)) for b in bound[:-1]]
    legend_labels = ['{} - {}'.format(int(bound_prep[i]), int(bound_prep[i+1])) for i in range(len(column_labels))]

    return patches, legend_labels


def cr_plot(data, row_labels, column_labels, output_path, default_val=0, width=15, colormap=None, graph_aspect=0.15, set_max=False, title=None):
    if len(row_labels) < 2:
        raise ValueError('Number of subplots must be greater than 1, plot manually')

    figw = width
    figh = figw * graph_aspect

    data = np.nan_to_num(data, nan=default_val) # comment out for gray spots on graph for NAN
    colormap = 'Wistia' if colormap is None else colormap # find out how to pass in colormap
    bound, bound_prep = bound_creation(data, column_labels)
    norm = plt.Normalize(vmin= data.min(), vmax= data.max())
    cmap = plt.cm.get_cmap(colormap, len(column_labels))
    gridspec_kw = {"height_ratios": [1] * len(row_labels), "width_ratios" : [1]}
    fig, axes = plt.subplots(ncols=1, nrows=len(row_labels), figsize=(figw, figh), gridspec_kw=gridspec_kw, sharey=True, sharex=True)

    for i, ax in enumerate(axes):
        dat = np.asarray(data[i,:]).reshape(1, data.shape[1])
        im = ax.imshow(dat, cmap=cmap, aspect=0.3, norm=norm)
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
           loc=(1.1, 1), title=r"$\bf{" + title + "}$")
    plt.savefig(output_path)

def yaxis_coords(number_of_subplots):
    first = -0.07 - (0.01 * number_of_subplots)
    second = 0.55 - (0.1 * number_of_subplots)
    return (first, second)
