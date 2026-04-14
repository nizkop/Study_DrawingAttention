import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch

from HelperFunctions.diagrams.basic_boxplot import box_plot_core, add_legend
from HelperFunctions.diagrams.get_color import get_color


def comparision_boxplot_across_groups(df: pd.DataFrame, y_column: str, y_label: str, x_label: str):
    df = df.sort_values("id")

    box_width = 0.2
    markersize = 3
    offsets = {
        "total": -1.5 * box_width,
        "Formula construction": -0.5 * box_width,
        "Static sketch construction": 0.5*box_width,
        "Dynamic sketch construction": 1.5*box_width
    }

    grouped_info_total = df.groupby('id')[y_column].apply(list).to_dict()
    x_values_total = [x+offsets["total"] for x in grouped_info_total.keys()]

    group_info_dict = {}
    for group, group_df in df.groupby("group", sort=False):
        group_info_dict[group] = group_df.groupby('id')[y_column].apply(list).to_dict()

    fig, ax = plt.subplots(figsize=(6.4*2, 4.8))
    # Total:
    box_plot_core(ax=ax, x_values=x_values_total, y_values=grouped_info_total.values(), color_label="total",
                  width=box_width, markersize=markersize)

    # Groups:
    groups = list(group_info_dict.keys())
    labels = ["All Groups"]
    for i, group in enumerate(groups):
        if i >= 3:
            break
        info = group_info_dict[group]
        x_values = [x+offsets[group] for x in info.keys()]
        box_plot_core(ax=ax, x_values=x_values, y_values=info.values(), color_label=group,
                      width=box_width, markersize=markersize)
        labels.append(group)

    # Set x-labels and x-ticks only once for a task (mean of offsets):
    x_positions = [x for x in grouped_info_total.keys()]
    ax.set_xticks(x_positions)
    ax.set_xticklabels(x_positions)

    for i in range(len(x_positions) - 1):
        x_mid = (x_positions[i] + x_positions[i + 1]) / 2
        ax.axvline(x=x_mid, color='gray', linestyle='--', linewidth=1, alpha=0.7)

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    legend = add_legend(ax=ax, color_label="total", markersize=markersize)
    ax.add_artist(legend)

    legend = legend_of_groups(ax=ax, labels=labels)
    ax.add_artist(legend)

    return fig, ax, legend


def legend_of_groups(ax, labels):
    legend_elements = [
        Patch(facecolor=get_color(label), edgecolor="none", label=label, alpha=0.7) for label in labels
    ]
    return ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=4)