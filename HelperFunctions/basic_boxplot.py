from matplotlib import pyplot as plt

from HelperFunctions.comparision_plot_mean import comparision_plot_mean


def basic_boxplot(x_values:list[float], y_values:list[list[float]],
                  y_label:str = "", x_label:str = ""):
    # --- Plot Box Plot ---
    fig, ax = plt.subplots()
    ax.boxplot(y_values, labels=x_values, patch_artist=True)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)
    fig.tight_layout()
    # plt.show()

    comparision_plot_mean(x_values=x_values, y_values=y_values, y_label=y_label, x_label=x_label)
    return fig, ax

