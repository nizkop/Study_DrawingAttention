
from HelperFunctions.get_data import get_data
from HelperFunctions.save_figures import save_figures
from HelperFunctions.diagrams.plot_combined_boxplots import plot_combined_boxplots
from HelperFunctions.diagrams.comparision_boxplot_across_groups import comparision_boxplot_across_groups
from StudyElements.Participant import Participant
from HelperFunctions.diagrams.basic_boxplot import basic_boxplot


def display_category(category:str, task_ids: list[int], participants: list[Participant]):
    if category == "TTU":
        y_label = "Time for Understanding [s]"
    elif category == "DOU":
        y_label = "Degree of Understanding [ ]"
    else:
        raise ValueError("Category unknown")

    df = get_data(participants=participants, task_ids=task_ids)
    df["id"] = df["id"].apply(lambda x: x.replace("task_", "")).astype(int)


    ### SEPARATE PLOTS ################################################################################################
    fig, ax, legend = basic_boxplot(df=df, color_label="total", y_column=category,
                  y_label=y_label, x_label="Task ID [ ]")
    save_figures(title=f"{category}_total", fig=fig, axes=ax, bbox_extra_artists=[legend])

    for group, participants_df in df.groupby("group", sort=False):
        fig, ax, legend =  basic_boxplot(df=participants_df, color_label=group, y_column=category,
                  y_label=y_label, x_label="Task ID [ ]")
        save_figures(title=f"TTU_{group.replace(' ','')}", fig=fig, axes=ax, bbox_extra_artists=[legend])

    ### COMBINED PLOTS ###############################################################################################
    fig, axes, legend = plot_combined_boxplots(df=df, y_column=category, y_label=y_label, x_label="Task ID [ ]")
    if category == "TTU":
        for ax in axes:
            # ax.set_yscale('log')
            # ax.set_ylim(top=3000)
            # ODER:
            ax.set_ylim(bottom=0, top=300)
    save_figures(fig=fig, axes=axes, title=f"{category}_overview_all_boxplots", bbox_extra_artists=[legend])


    fig, ax, legend = comparision_boxplot_across_groups(df=df, y_column=category, y_label=y_label, x_label="Task ID [ ]")
    ax.set_ylim(bottom=0, top=300)
    save_figures(fig=fig, axes=ax, title=f"{category}_comparision_boxplot_across_groups", bbox_extra_artists=[legend])

    return


