import pandas as pd

from HelperFunctions.statistics.between_subjects_anova import between_subjects_anova
from HelperFunctions.statistics.post_hoc_within import post_hoc_within
from HelperFunctions.statistics.within_subjects_anova import within_subjects_anova
from StudyElements.Participant import Participant
from HelperFunctions.basic_boxplot import basic_boxplot
from compact_letter_display import compact_letter_display


def display_DOU(task_ids: list[int], participants: list[Participant]):
    x_values = []
    y_values = []
    data = []
    for task_id in task_ids:
        x_values.append(task_id)
        y_values.append([])
        for p in participants:
            task = p.get_participant_task(task_id=task_id)
            if task is not None:
                y_values[-1].append(task.degree_of_understanding)
                data.append({
                    "id": f"task_{task.task_number}",
                    "group": p.studygroup.value,
                    "DOU": task.degree_of_understanding,
                    "dummy": 1
                })
            else:
                raise Exception(f"missing task {p.id}_{task_id}")

    fig, ax = basic_boxplot(x_values=x_values, y_values=y_values,
                  y_label="Degree of Understanding [ ]", x_label="Task ID")
    fig.savefig("DOU_total.pdf", bbox_inches="tight")


    df = pd.DataFrame(data)
    df_agg, result_total = within_subjects_anova(df=df, print_info=False, try_again=True, value_col="DOU",
                                                 potential_difference_determining_column="group", subject_col="id")
    print(result_total)
    sig_matrix, groups, n = post_hoc_within(df_agg, group_col="group", value_col="DOU", subject_col="id")
    cld_strings_total = compact_letter_display(groups, n, sig_matrix, print_info=True)

    df = pd.DataFrame(data)
    result = between_subjects_anova(df=df, print_info=False, value_col="DOU",
                                                 potential_difference_determining_column="id")
    # print(result_total)
    # sig_matrix, groups, n = post_hoc_for_one_way_anova(groups, group_col="id", value_col="measured_value")
    # cld_strings_total = compact_letter_display(groups, n, sig_matrix, print_info=True)
