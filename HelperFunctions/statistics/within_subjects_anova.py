from statsmodels.stats.anova import AnovaRM

from HelperFunctions.statistics.get_partial_ETA_squared import get_partial_ETA_squared
from SETTINGS import alpha


def within_subjects_anova(df, potential_difference_determining_column:str,
                          try_again=False, print_info:bool=True):
    if df.empty:
        print("⚠️ DataFrame ist leer – keine ANOVA möglich.")
        return None, None

    df_agg = (
        df.groupby(["id", potential_difference_determining_column], as_index=False)["measured_value"]
          .mean()
    )
    try:
        aov = AnovaRM(df_agg, depvar="measured_value", subject="id", within=[potential_difference_determining_column])
        res = aov.fit()

        if print_info:
            print("\n\t=== Repeated‑Measures ANOVA ===")
            print("\t", str(res).replace("\n","\n\t"), sep="")

        partial_eta_squared = get_partial_ETA_squared(res)

        p_val = res.anova_table["Pr > F"].iloc[0]
        if p_val < alpha:
            result = f"→ signifikanter Unterschied zwischen sketch & voice (p = {p_val:.4g}, eta = {partial_eta_squared:.4g}))"
            # Tendency:
            # Medianberechnung
            medians = df.groupby(potential_difference_determining_column)["measured_value"].median()
            sorted_medians = medians.sort_values()
            result += "\n\t\u001b[1m→ Median Werte aller Gruppen:\u001b[0m"
            for group_name, median_val in sorted_medians.items():
                result += f"\n\t  {group_name:10} → {median_val:.3f} s"
        else:
            result = f"→ kein signifikanter Unterschied (p = {p_val:.4g}, eta = {partial_eta_squared:.4g}))"
        return df_agg, result
    except ValueError:
        # Data is unbalanced
        print("! Task-ID is missing sketch/voice data point -> shortening data:", end="\t", flush=True)
        if try_again:
            return None, None
        # Nur IDs behalten, die alle Modalitäten haben:
        complete_ids = (
            df.groupby("id")[potential_difference_determining_column].nunique()  # wie viele Modalitäten je ID?
            .eq(df[potential_difference_determining_column].nunique())  # gleich der Gesamtzahl?
        )
        df_balanced = df[df["id"].isin(complete_ids[complete_ids].index)]

        #Info: welche IDs bleiben nach der Filterung übrig
        remaining_ids = sorted(df_balanced["id"].unique())
        print(f"→ {len(remaining_ids)} complete tasks remaining: {remaining_ids}")
        return within_subjects_anova(df=df_balanced, try_again=True, print_info=print_info,
                                     potential_difference_determining_column=potential_difference_determining_column)
