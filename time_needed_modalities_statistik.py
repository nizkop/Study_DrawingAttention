import pandas as pd
from statsmodels.stats.anova import AnovaRM
import itertools
import numpy as np
from scipy import stats
from statsmodels.stats.multitest import multipletests

from SETTINGS import alpha
from get_partial_ETA_squared import get_partial_ETA_squared


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
            print("\n=== Repeated‑Measures ANOVA ===")
            print(res)

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
            result = f"→ kein signifikanter Unterschied (p = {p_val:.4g},, eta = {partial_eta_squared:.4g}))"
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
        return within_subjects_anova(df=df_balanced, alpha=alpha, try_again=True, print_info=print_info)



def post_hoc_within(data_tbl: pd.DataFrame,
                    value_col: str ="time",
                    group_col: str = "modality",
                    subject_col: str = "id"
                    ):
    """
    Pairwise, dependent (paired) t‑tests for a within‑subjects design.
    Returns a significance matrix (True = no significant difference),
    the list of group names and the number of groups (n).
    """
    if data_tbl is None or data_tbl.empty:
        return None, None, None
    groups = data_tbl[group_col].unique()
    n_groups = len(groups)

    p_matrix = np.ones((n_groups, n_groups))

    # für jedes Paar (i,j) gepaarten t‑Test durchführen:
    for (i, g1), (j, g2) in itertools.combinations(enumerate(groups), 2):
        d1 = data_tbl.loc[data_tbl[group_col] == g1].set_index(subject_col)[value_col]
        d2 = data_tbl.loc[data_tbl[group_col] == g2].set_index(subject_col)[value_col]
        common = d1.index.intersection(d2.index)
        d1, d2 = d1.loc[common], d2.loc[common]

        # gepaarter t‑Test
        tstat, p = stats.ttest_rel(d1, d2)
        p_matrix[i, j] = p
        p_matrix[j, i] = p

    triu_idx = np.triu_indices(n_groups, k=1)
    p_vals = p_matrix[triu_idx]

    assert len(p_vals) > 0, "No p-values available for multiple testing correction!"

    reject, p_corr, _, _ = multipletests(p_vals, alpha=alpha, method="holm")
    p_matrix[triu_idx] = p_corr
    p_matrix[(triu_idx[1], triu_idx[0])] = p_corr   # spiegeln
    sig_matrix = p_matrix > alpha

    return sig_matrix, list(groups), n_groups




