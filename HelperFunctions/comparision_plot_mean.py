from matplotlib import pyplot as plt
from numpy import mean


def comparision_plot_mean(info:dict, y_label:str = "", x_label:str = ""):
    # --- Plot MEAN to compare to K.'s Plots ---
    y_values = info.values()
    x_values = [int(i.replace("task_","")) for i in info.keys()]

    fig2, ax2 = plt.subplots()
    y_mean_values = [mean(y) for y in y_values]
    ax2.bar(x_values, y_mean_values, color='blue', edgecolor='black')
    ax2.set_xticks(x_values)
    ax2.set_xlabel(x_label)
    ax2.set_ylabel(y_label)
    ax2.grid(True, axis='y', linestyle='--', alpha=0.7)
    fig2.tight_layout()
    # plt.show()