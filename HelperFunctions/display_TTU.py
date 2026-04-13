import pandas as pd

from StudyElements.Participant import Participant
from HelperFunctions.basic_boxplot import basic_boxplot
from compact_letter_display import compact_letter_display
from HelperFunctions.statistics.post_hoc_within import post_hoc_within
from HelperFunctions.statistics.within_subjects_anova import within_subjects_anova


def display_TTU(task_ids: list[int], participants: list[Participant]):
    x_values = []
    y_values = []
    data = []
    for task_id in task_ids:
        x_values.append(task_id)
        y_values.append([])
        for p in participants:
            task = p.get_participant_task(task_id=task_id)
            if task is not None:
                if task.degree_of_understanding > 0 and not task.skipped:
                    y_values[-1].append(task.time_to_understand)
                    data.append({
                        "id": f"task_{task.task_number}",
                        "group": p.studygroup.value,
                        "TTU": task.time_to_understand,
                    })
            else:
                raise Exception(f"missing task {p.id}_{task.task_number}")

    fig, ax = basic_boxplot(x_values=x_values, y_values=y_values,
                  y_label="Time to Understand [s]", x_label="Task ID")
    fig.savefig("TTU_total.pdf", bbox_inches="tight")

    df = pd.DataFrame(data)
    df_agg, result_total = within_subjects_anova(df=df, print_info=False, try_again=True, value_col="TTU",
                                                 potential_difference_determining_column="group")
    print(result_total)
    sig_matrix, groups, n = post_hoc_within(df_agg, group_col="group", value_col="TTU", subject_col="id")
    cld_strings_total = compact_letter_display(groups, n, sig_matrix, print_info=True)
