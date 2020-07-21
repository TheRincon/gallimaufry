import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)

def bar_and_data_plot(x, y, output_path, bar_width=0.5, bar_colors=['#FC8D62','#65C2A5'], edge_colors=None):
    fig, ax = plt.subplots()
    ax.bar(x,
           height=[np.mean(yi) for yi in y],
           yerr=[np.std(yi) for yi in y],    # error bars
           capsize=12, # error bar cap width in points
           width=bar_width,
           tick_label=["control", "test"],
           color=bar_colors,  # for face color transparent = (0,0,0,0)
           edgecolor=colors,
           # ecolor=colors,    # error bar colors; setting this raises an error for whatever reason.
           )

    for i in range(len(x)):
        ax.scatter(x[i] + np.random.random(y[i].size) * bar_width - bar_width / 2, y[i], color='black', zorder=99)

    # plt.show()
    plt.savefig(output_path)

if __name__ == '__main__':
    bar_width = 0.5
    bar_coordinates = [1, 2]
    colors = ['#FC8D62','#65C2A5']
    data = [np.random.random(30) * 2 + 5, np.random.random(10) * 3 + 8]
    bar_and_data_plot(bar_coordinates, data, 'bar_points.png', bar_width=bar_width, bar_colors=colors, edge_colors=None)
