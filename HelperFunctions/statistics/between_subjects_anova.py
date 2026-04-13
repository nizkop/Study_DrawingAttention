from scipy.stats import f_oneway
from SETTINGS import alpha


def between_subjects_anova(df, potential_difference_determining_column: str, value_col="measured_value",
                  print_info: bool = True):
    if df.empty:
        print("⚠️ DataFrame ist leer – keine ANOVA möglich.")
        return None, None
    # TODO