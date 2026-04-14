import matplotlib.pyplot as plt
import pandas as pd

from HelperFunctions.basic_boxplot import box_plot_core, add_legend


def plot_combined_boxplots(df:pd.DataFrame, y_column:str, y_label: str, x_label: str):
    """
    Overview of 4 Boxplots: total data, Group F, Group S, Group V
    """
    df = df.sort_values("id")

    grouped_info_total = df.groupby('id')[y_column].apply(list).to_dict()
    x_values_total = [int(i) for i in grouped_info_total.keys()]

    group_info_dict = {}
    for group, group_df in df.groupby("group", sort=False):
        group_info_dict[group] = group_df.groupby('id')[y_column].apply(list).to_dict()


    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()

    # Total:
    box_plot_core(ax=axes[0], x_values=x_values_total, y_values=grouped_info_total.values(), color_label="total")
    axes[0].set_title("All Groups", fontweight='bold')
    axes[0].set_xlabel(x_label)
    axes[0].set_ylabel(y_label)

    # Groups:
    groups = list(group_info_dict.keys())
    for i, group in enumerate(groups):
        if i >= 3:
            break
        info = group_info_dict[group]
        x_values = [i for i in info.keys()]
        box_plot_core(ax=axes[i + 1], x_values=x_values, y_values=info.values(), color_label=group)
        axes[i + 1].set_title(f"Group \"{group}\"", fontweight='bold')
        axes[i + 1].set_xlabel(x_label)
        axes[i + 1].set_ylabel(y_label)

    legend = add_legend(ax=axes[0], color_label="total")
    return fig, axes, legend