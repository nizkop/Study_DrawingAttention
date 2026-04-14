import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from numpy import mean

from HelperFunctions.diagrams.comparision_plot_mean import comparision_plot_mean
from HelperFunctions.diagrams.get_color import get_color


def basic_boxplot(df:pd.DataFrame, y_column:str, color_label:str=None,
                  y_label:str = "", x_label:str = ""):
    df = df.sort_values("id")

    grouped_info = df.groupby('id')[y_column].apply(list).to_dict()
    x_values = [int(i) for i in grouped_info.keys()]
    y_values = grouped_info.values()

    # --- Plot Box Plot ---
    fig, ax = plt.subplots()
    box_plot_core(ax=ax, x_values=x_values, y_values=y_values, color_label=color_label)
    legend = add_legend(ax, color_label)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    comparision_plot_mean(df=df, y_column=y_column, y_label=y_label, x_label=x_label)
    return fig, ax, legend



def box_plot_core(ax, x_values, y_values, color_label:str="", width=None, markersize=6):
    mean_values = [ mean(y) for y in y_values]
    if width is None:
        ax.boxplot(y_values, positions=x_values, patch_artist=True,
                   boxprops=dict(facecolor=get_color(color_label), edgecolor="none", alpha=0.7),
                   medianprops=dict(color=get_color("median")),
                   whiskerprops=dict(color='black'), capprops=dict(color='black'),
                   flierprops=dict(color='black', markeredgecolor='black', markersize=markersize)
                   )
    else:
        ax.boxplot(y_values, positions=x_values, patch_artist=True, widths=width,
                   boxprops=dict(facecolor=get_color(color_label), edgecolor="none", alpha=0.7),
                   medianprops=dict(color=get_color("median")),
                   whiskerprops=dict(color='black'), capprops=dict(color='black'),
                   flierprops=dict(color='black', markeredgecolor='black', markersize=markersize)
                   )
    ax.plot(x_values, mean_values, marker='o', color=get_color("mean"), linestyle='None',
            label='Mean', markeredgecolor='none', markersize=markersize)

    return


def add_legend(ax, color_label:str, markersize=6):
    """
    Adds explanatory legend for box plot items
    """
    legend_elements = [
        Line2D([0], [0], color=get_color("median"), linewidth=2, label='Median'),
        Line2D([0], [0], marker='o', color=get_color("mean"), markersize=markersize, linestyle='None',
               markeredgecolor='none', label='Mean'),
        Patch(facecolor=get_color(color_label), edgecolor="none", label='IQR: [$Q_1, Q_3$]', alpha=0.7),
        Line2D([0], [0], color='black', linewidth=1.5, label=r'[$Q_1 - 1.5\cdot IQR,$' + "\n   " + r'$Q_3 + 1.5\cdot IQR$]'),
        Line2D([0], [0], marker='o', color='black', markersize=markersize, linestyle='None',
               markerfacecolor='none', markeredgecolor='black', label='Potential Outliers'),
    ]
    return ax.legend(handles=legend_elements, loc='best')
