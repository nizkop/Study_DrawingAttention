import pandas as pd

from StudyElements.Participant import Participant
from HelperFunctions.basic_boxplot import basic_boxplot
from compact_letter_display import compact_letter_display
from time_needed_modalities_statistik import within_subjects_anova, post_hoc_within


def display_DOU(task_ids: list[int], participants: list[Participant]):
    if participants is None:
        raise ValueError("Participants list must be provided.")

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
                    "measured_value": task.degree_of_understanding,
                })
            else:
                raise Exception(f"missing task {p.id}_{task_id}")

    fig, ax = basic_boxplot(x_values=x_values, y_values=y_values,
                  y_label="Degree of Understanding [ ]", x_label="Task ID")
    fig.savefig("DOU_total.pdf", bbox_inches="tight")


    df = pd.DataFrame(data)
    df_agg, result_total = within_subjects_anova(df=df, print_info=True, try_again=True,
                                                 potential_difference_determining_column="group")
    print(result_total)
    sig_matrix, groups, n = post_hoc_within(df_agg, group_col="group", value_col="measured_value", subject_col="id")
    cld_strings_total = compact_letter_display(groups, n, sig_matrix, print_info=True)

