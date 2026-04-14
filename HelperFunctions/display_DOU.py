import pandas as pd

from HelperFunctions.get_data import get_data
from HelperFunctions.save_figures import save_figures
from HelperFunctions.statistics.between_subjects_anova import between_subjects_anova
from HelperFunctions.statistics.post_hoc_within import post_hoc_within
from HelperFunctions.statistics.within_subjects_anova import within_subjects_anova
from StudyElements.Participant import Participant
from HelperFunctions.basic_boxplot import basic_boxplot
from compact_letter_display import compact_letter_display


def display_DOU(task_ids: list[int], participants: list[Participant]):
    df = get_data(participants=participants, task_ids=task_ids)

    grouped_info = df.groupby('id')['DOU'].apply(list).to_dict()
    fig, ax = basic_boxplot(info=grouped_info, color_label="total",
                            y_label="Degree of Understanding [s]", x_label="Task ID")
    save_figures(title="DOU_total", fig=fig, ax=ax)


    df_agg, result_total = within_subjects_anova(df=df, print_info=False, try_again=True, value_col="DOU",
                                                 potential_difference_determining_column="group", subject_col="id")
    print(result_total)
    sig_matrix, groups, n = post_hoc_within(df_agg, group_col="group", value_col="DOU", subject_col="id")
    cld_strings_total = compact_letter_display(groups, n, sig_matrix, print_info=True)


    result = between_subjects_anova(df=df, print_info=False, value_col="DOU",
                                                 potential_difference_determining_column="id")
    # print(result_total)
    # sig_matrix, groups, n = post_hoc_for_one_way_anova(groups, group_col="id", value_col="measured_value")
    # cld_strings_total = compact_letter_display(groups, n, sig_matrix, print_info=True)


    for group, participants_df in df.groupby("group", sort=False):
        grouped_info = participants_df.groupby('id')['DOU'].apply(list).to_dict()
        fig, ax = basic_boxplot(info=grouped_info,color_label=group,
                                y_label="Degree of Understanding [s]", x_label="Task ID")
        save_figures(title=f"DOU_{group.replace(' ','')}", fig=fig, ax=ax)
