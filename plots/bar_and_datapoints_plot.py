import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)

def bar_and_data_plot(x, y, output_path, tick_labels, bar_width=0.5, bar_colors=['#FC8D62','#65C2A5'], edge_colors=None):
    fig, ax = plt.subplots()
    ax.bar(x,
           height=[np.mean(yi) for yi in y],
           yerr=[np.std(yi) for yi in y],    # error bars
           capsize=12, # error bar cap width in points
           width=bar_width,
           tick_label=tick_labels,
           color=bar_colors,  # for face color transparent = (0,0,0,0)
           edgecolor=colors,
           # ecolor=colors,    # error bar colors; setting this raises an error for whatever reason.
           )

    for i in range(len(x)):
        ax.scatter(x[i] + np.random.random(y[i].size) * bar_width - bar_width / 2, y[i], color='black', zorder=99)

    plt.savefig(output_path)
