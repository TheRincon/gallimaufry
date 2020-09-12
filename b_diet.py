import pandas as pd
import matplotlib.pyplot as plt
import math
import os
import colorer as colo
import matplotlib as mpl
from PIL import Image, ImageDraw
from matplotlib.cbook import get_sample_data

from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

mpl.rcParams.update({'figure.autolayout': True})

mpl.rcParams['figure.dpi'] = 200
plt.rc_context({'ytick.color':'gray'})

# https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
SMALL_SIZE = 5
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)
plt.rc('axes', titlesize=SMALL_SIZE)
plt.rc('axes', labelsize=MEDIUM_SIZE)
plt.rc('xtick', labelsize=SMALL_SIZE)
plt.rc('ytick', labelsize=SMALL_SIZE)
plt.rc('legend', fontsize=SMALL_SIZE)
plt.rc('figure', titlesize=BIGGER_SIZE)

def center_cropped(w, h, original):
    width, height = original.size
    # assert (w <= width), 'Cropped image width must be smaller or equal to original image width!'
    # assert (h <= height), 'Cropped image height must be smaller or equal to original image height!'
    x_offset = (width - w) / 2
    y_offset = (height - h) / 2
    left = x_offset
    right = width - x_offset + 113
    top = (height - y_offset) * 1.2
    bottom = y_offset
    cropped = original.crop((left, bottom, right, top))
    return cropped

def get_dims(bars):

    fig = plt.gcf()
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    heights = [bar.get_window_extent(r).height for bar in bars]
    widths = [bar.get_window_extent(r).width for bar in bars]
    return widths, heights

# def paste_image(x, y, img):
#     ax = plt.gca()
#     imagebox = OffsetImage(img, zoom=0.2)
#     ab = AnnotationBbox(imagebox, (x, y), frameon=False)
#     ab.zorder = 49
#     ax.add_artist(ab)

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
def ding_an_sich_plot(
    df,
    width=0.9,
    color='#D3D3D3',
    xlabel='',
    ylabel='',
    title='',
    pad_height=5,
    label_shift=0.45,
    image_array=None
):

    list_columns = df.columns.tolist()
    labels = list(df.groupby(['Label']).groups.keys())
    category_sums = df.groupby(['Category'], as_index=False)[['Amount']].sum()
    category_labels = list(df.groupby(['Category']).groups.keys())
    indices = range(len(df['Category'].unique()))
    xlocs = [i for i in indices]

    big_bars = plt.bar(indices, category_sums['Amount'].tolist(), width=width,
            color=color, label='Category Sums', zorder=50)

    large_widths, large_heights = get_dims(big_bars)

    original = Image.open('/home/rincon/Downloads/Lenna.png')
    for g in indices:
        cropped = center_cropped(large_widths[g], large_heights[g], original)
        ax = plt.gca()
        imagebox = OffsetImage(cropped, zoom=0.2)
        ab = AnnotationBbox(imagebox, (g, category_sums['Amount'].tolist()[g] / 2), frameon=False)
        ab.zorder = 49
        ax.add_artist(ab)

    for i, x in category_sums.iterrows():
        plt.text(xlocs[i] - label_shift, x['Amount'] + pad_height, x['Category'], wrap=True)

    graph_locs = []
    graph_labs = []

    for ind in indices:
        label = category_labels[ind]
        label_locs = df.loc[df.Category == label].sort_values(by=['Amount'], ascending=False)
        cat_len = len(label_locs)
        locs = subplot_locations(1 / (cat_len * 2), ind, cat_len, width)
        graph_locs.extend(locs)
        graph_labs.extend(label_locs['Label'].tolist())
        bars = plt.bar(
            locs,
            label_locs['Amount'].tolist(),
            width=(1 / cat_len) * width,
            color=label_locs['Color'].tolist(),
            alpha=1.0,
            zorder=55,
            tick_label=label_locs['Label'].tolist()
        )

        smal_widths, small_heights = get_dims(bars)

    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=20)
    plt.xticks(graph_locs, graph_labs, rotation=45, ha="right")
    plt.box(False)
    axes = plt.gca()
    axes.yaxis.grid(alpha=0.5, zorder=0)
    # plt.draw()

    return plt

def subplot_locations(shim, index, category_len, width):
    y = mirror_numbers_graphing(category_len, shim, index, width)
    return [x for x in y]

def save_figure(fig, output_dir, filename, pad_inches=0.3):
    fig.savefig(os.path.join(output_dir, filename),
                # dpi=fig.dpi,
                bbox_inches='tight',
                pad_inches=pad_inches)
    plt.clf()


if __name__ == '__main__':
    lb = pd.read_csv('/home/rincon/Desktop/Animal_Diets/large_birds.csv', sep=',')
    plotted_lb = ding_an_sich_plot(
        lb,
        color=['#F9E4B7', '#996515', '#996515', '#545454', '#545454', '#232B2B'],
        ylabel='Grams / Day',
        title='Large Bird Diets',
        label_shift=0.40,
        image_array=['/home/rincon/Desktop/Downloads/lynx.jpg']
    )
    plotted_lb.show()
    save_figure(plotted_lb, '/home/rincon/Desktop/Workspace/gallimaufry/output/', 'Large_Bird_Diets.png')
    colo.resizer(
        '/home/rincon/Desktop/Workspace/gallimaufry/output/Large_Bird_Diets.png',
        2000,
        2000,
        '#FFFFFF',
        '/home/rincon/Desktop/Workspace/gallimaufry/output/Large_Bird_Diets_Resized.png'
    )
    #
    # mb = pd.read_csv('/home/rincon/Desktop/medium_birds.csv', sep=',')
    # plotted_mb = ding_an_sich_plot(
    #     mb,
    #     color=[ '#FFB347', '#882D17', '#36454F', '#E2DCCD', '#420D09'],
    #     ylabel='Grams / Day',
    #     title='Medium Bird Diets',
    #     pad_height=2
    # )
    # save_figure(plotted_mb, '/home/rincon/Desktop/Workspace/gallimaufry/output/', 'Medium_Bird_Diets.png')
    # colo.resizer(
    #     '/home/rincon/Desktop/Workspace/gallimaufry/output/Medium_Bird_Diets.png',
    #     2000,
    #     2000,
    #     '#FFFFFF',
    #     '/home/rincon/Desktop/Workspace/gallimaufry/output/Medium_Bird_Diets_Resized.png'
    # )
    #
    # sb = pd.read_csv('/home/rincon/Desktop/small_birds.csv', sep=',')
    # plotted_sb = ding_an_sich_plot(
    #     sb,
    #     color=[ '#003366', '#003366', '#CC5500', '#CC5500', '#FFFF00', '#FFFF00'],
    #     ylabel='Grams / Day',
    #     title='Small Bird Diets',
    #     pad_height=0.5
    # )
    # save_figure(plotted_sb, '/home/rincon/Desktop/Workspace/gallimaufry/output/', 'Small_Bird_Diets.png')
    # colo.resizer(
    #     '/home/rincon/Desktop/Workspace/gallimaufry/output/Small_Bird_Diets.png',
    #     2000,
    #     2000,
    #     '#FFFFFF',
    #     '/home/rincon/Desktop/Workspace/gallimaufry/output/Small_Bird_Diets_Resized.png'
    # )
    #
    # im_concat = colo.concat_v(
    #     '/home/rincon/Desktop/Workspace/gallimaufry/output/Small_Bird_Diets_Resized.png',
    #     '/home/rincon/Desktop/Workspace/gallimaufry/output/Medium_Bird_Diets_Resized.png',
    #     '/home/rincon/Desktop/Workspace/gallimaufry/output/Small_And_Medium_Bird_Diets_Concat.png'
    # )
    #
    # colo.concat_v(
    #     im_concat,
    #     '/home/rincon/Desktop/Workspace/gallimaufry/output/Large_Bird_Diets_Resized.png',
    #     '/home/rincon/Desktop/Workspace/gallimaufry/output/Small_And_Medium_And_Large_Bird_Diets_Concat.png'
    # )
    #
    # im_concat_h = colo.concat_h(
    #     im1,
    #     im2,
    #     '/home/rincon/Desktop/Workspace/gallimaufry/output/Small_And_Medium_Bird_Diets_Concat_h.png'
    # )
    #
    # colo.concat_h(
    #     im_concat_h,
    #     '/home/rincon/Desktop/Workspace/gallimaufry/output/Large_Bird_Diets_Resized.png',
    #     '/home/rincon/Desktop/Workspace/gallimaufry/output/Small_And_Medium_And_Large_Bird_Diets_Concat_h.png'
    # )
