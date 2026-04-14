
from HelperFunctions.get_data import get_data
from HelperFunctions.save_figures import save_figures
from HelperFunctions.diagrams.plot_combined_boxplots import plot_combined_boxplots
from HelperFunctions.diagrams.comparision_boxplot_across_groups import comparision_boxplot_across_groups
from StudyElements.Participant import Participant
from HelperFunctions.diagrams.basic_boxplot import basic_boxplot
from compact_letter_display import compact_letter_display
from HelperFunctions.statistics.post_hoc_within import post_hoc_within
from HelperFunctions.statistics.within_subjects_anova import within_subjects_anova


def display_TTU(task_ids: list[int], participants: list[Participant]):
    df = get_data(participants=participants, task_ids=task_ids)
    df["id"] = df["id"].apply(lambda x: x.replace("task_", "")).astype(int)

    fig, ax, legend = basic_boxplot(df=df, color_label="total", y_column="TTU",
                  y_label="Time for Understanding [s]", x_label="Task ID [ ]")
    save_figures(title="TTU_total", fig=fig, axes=ax, bbox_extra_artists=[legend])


    df_agg, result_total = within_subjects_anova(df=df, print_info=False, try_again=True, value_col="TTU",
                                                 potential_difference_determining_column="group")
    print(result_total)
    sig_matrix, groups, n = post_hoc_within(df_agg, group_col="group", value_col="TTU", subject_col="id")
    cld_strings_total = compact_letter_display(groups, n, sig_matrix, print_info=True)

    for group, participants_df in df.groupby("group", sort=False):
        fig, ax, legend =  basic_boxplot(df=participants_df, color_label=group, y_column="TTU",
                  y_label="Time for Understanding [s]", x_label="Task ID [ ]")
        save_figures(title=f"TTU_{group.replace(' ','')}", fig=fig, axes=ax, bbox_extra_artists=[legend])

    fig, axes, legend = plot_combined_boxplots(df=df, y_column="TTU", y_label="Time for Understanding [s]", x_label="Task ID [ ]")
    for ax in axes:
        # ax.set_yscale('log')
        # ax.set_ylim(top=3000)
        # ODER:
        ax.set_ylim(bottom=0, top=300)
    save_figures(fig=fig, axes=axes, title="TTU_overview_all_boxplots", bbox_extra_artists=[legend])

    df_low = df[df["id"] <= 9]
    df_high = df[df["id"] > 9]
    fig, ax, legend = comparision_boxplot_across_groups(df=df, y_column="TTU", y_label="Time for Understanding [s]", x_label="Task ID [ ]")
    ax.set_ylim(bottom=0, top=300)
    save_figures(fig=fig, axes=ax, title="TTU_comparision_boxplot_across_groups", bbox_extra_artists=[legend])
