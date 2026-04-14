
from HelperFunctions.get_data import get_data
from HelperFunctions.save_figures import save_figures
from StudyElements.Participant import Participant
from HelperFunctions.basic_boxplot import basic_boxplot
from compact_letter_display import compact_letter_display
from HelperFunctions.statistics.post_hoc_within import post_hoc_within
from HelperFunctions.statistics.within_subjects_anova import within_subjects_anova


def display_TTU(task_ids: list[int], participants: list[Participant]):
    df = get_data(participants=participants, task_ids=task_ids)

    grouped_info = df.groupby('id')['TTU'].apply(list).to_dict()
    fig, ax = basic_boxplot(info=grouped_info, color_label="total",
                  y_label="Time for Understanding [s]", x_label="Task ID")
    save_figures(title="TTU_total", fig=fig, ax=ax)


    df_agg, result_total = within_subjects_anova(df=df, print_info=False, try_again=True, value_col="TTU",
                                                 potential_difference_determining_column="group")
    print(result_total)
    sig_matrix, groups, n = post_hoc_within(df_agg, group_col="group", value_col="TTU", subject_col="id")
    cld_strings_total = compact_letter_display(groups, n, sig_matrix, print_info=True)


    for group, participants_df in df.groupby("group", sort=False):
        grouped_info = participants_df.groupby('id')['TTU'].apply(list).to_dict()
        fig, ax = basic_boxplot(info=grouped_info,color_label=group,
                                y_label="Time for Understanding [s]", x_label="Task ID")
        save_figures(title=f"TTU_{group.replace(' ','')}", fig=fig, ax=ax)

