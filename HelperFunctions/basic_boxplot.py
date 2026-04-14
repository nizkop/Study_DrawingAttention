from matplotlib import pyplot as plt

from HelperFunctions.comparision_plot_mean import comparision_plot_mean
from HelperFunctions.get_color import get_color


def basic_boxplot(info:dict, color_label:str=None,
                  y_label:str = "", x_label:str = ""):
    # --- Plot Box Plot ---
    x_values = [i.replace("task_", "") for i in info.keys()]
    fig, ax = plt.subplots()
    ax.boxplot(info.values(), labels=x_values, patch_artist=True,
               boxprops=dict(facecolor=get_color(color_label), color='black'),
               )
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)
    fig.tight_layout()
    # plt.show()

    comparision_plot_mean(info=info, y_label=y_label, x_label=x_label)
    return fig, ax

