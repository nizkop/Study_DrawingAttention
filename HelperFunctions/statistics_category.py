

from HelperFunctions.get_data import get_data
from HelperFunctions.statistics.between_subjects_anova import between_subjects_anova
from StudyElements.Participant import Participant
from compact_letter_display import compact_letter_display
from HelperFunctions.statistics.post_hoc_within import post_hoc_within
from HelperFunctions.statistics.within_subjects_anova import within_subjects_anova


def statistics_category(category:str, task_ids: list[int], participants: list[Participant]):
    if category not in ["TTU", "DOU"]:
        raise ValueError("Category unknown")

    df = get_data(participants=participants, task_ids=task_ids)
    df["id"] = df["id"].apply(lambda x: x.replace("task_", "")).astype(int)

    results = f"DIFFERENCES IN \u001b[1m{category}\u001b[0m:\n"
    df_agg, result_total = within_subjects_anova(df=df, print_info=False, value_col=category,
                                                 potential_difference_determining_column="group", subject_col="id")
    results += "\t" + result_total + "\n"
    sig_matrix, groups, n = post_hoc_within(df_agg, group_col="group", value_col=category, subject_col="id")
    cld_strings_total = compact_letter_display(groups, n, sig_matrix, print_info=False)
    results += f"\tCompact-Letter-Display:  {cld_strings_total}\n"

    result = between_subjects_anova(df=df, print_info=False, value_col=category,
                                    potential_difference_determining_column="id")#TODO


    return results

