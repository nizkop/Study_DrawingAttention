from statsmodels.stats.anova import AnovaRM

from HelperFunctions.statistics.get_partial_ETA_squared import get_partial_ETA_squared
from SETTINGS import alpha, AGGREGATION_FUNCTION


def within_subjects_anova(df, potential_difference_determining_column:str, subject_col="id", value_col="measured_value",
                          print_info:bool=True):
    if df.empty:
        print("⚠️ DataFrame ist leer – keine ANOVA möglich.")
        return None, None

    if AGGREGATION_FUNCTION == "mean":
        df_agg = (
            df.groupby([subject_col, potential_difference_determining_column], as_index=False)[value_col]
              .median()
        )
    else:
        df_agg = (
            df.groupby([subject_col, potential_difference_determining_column], as_index=False)[value_col]
            .median()
        )

    try:
        aov = AnovaRM(df_agg, depvar=value_col, subject=subject_col, within=[potential_difference_determining_column])
        res = aov.fit()

        if print_info:
            print("\n\t=== Repeated‑Measures ANOVA ===")
            print("\t", str(res).replace("\n","\n\t"), sep="")

        partial_eta_squared = get_partial_ETA_squared(res)

        p_val = res.anova_table["Pr > F"].iloc[0]
        if p_val < alpha:
            result = f"→ Significant difference in {value_col} (p = {p_val:.4g}, eta = {partial_eta_squared:.4g}))"
            # Tendency by Median of Group:
            medians = df.groupby(potential_difference_determining_column)[value_col].median()
            sorted_medians = medians.sort_index()# sorted by group name
            result += "\n\t\t→ Median Values of all Groups:"
            for group_name, median_val in sorted_medians.items():
                if value_col == "TTU":
                    precision = 0# only int precision TUU (s)
                else:
                    precision = 3
                result += f"\n\t\t  - {group_name:10} → {median_val:.{precision}f} s"
        else:
            result = f"→ No significant difference (p = {p_val:.4g}, eta = {partial_eta_squared:.4g}))"
        return df_agg, result
    except ValueError:
        # Data is unbalanced
        print("! Task-ID is missing sketch/voice data point -> shortening data:", end="\t", flush=True)
        return
