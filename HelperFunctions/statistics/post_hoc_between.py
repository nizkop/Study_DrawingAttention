from scipy import stats
from statsmodels.stats.multitest import multipletests
import numpy as np
import itertools
import pandas as pd

from SETTINGS import alpha, AGGREGATION_FUNCTION


def post_hoc_between(data_tbl: pd.DataFrame,
                      value_col: str = "measured_value",
                      subject_col: str = "id"
                      ):
    """
    Pairwise, independent t-tests for a between-subjects design
    where groups are defined by subject_col (each subject is a group).

    :return sig_matrix: boolean matrix (True = no significant difference)
    :return groups: list of subject IDs (group names)
    :return n: number of groups (number of subjects)
    """
    if data_tbl is None or data_tbl.empty:
        return None, None, None
    groups = data_tbl[subject_col].unique()
    n_groups = len(groups)

    p_matrix = np.ones((n_groups, n_groups))

    # for each combination: independent t-test
    for (i, s1), (j, s2) in itertools.combinations(enumerate(groups), 2):
        d1 = data_tbl[data_tbl[subject_col] == s1][value_col]
        d2 = data_tbl[data_tbl[subject_col] == s2][value_col]

        # paired t‑test:
        if AGGREGATION_FUNCTION == "median":
            tstat, p = stats.mannwhitneyu(d1, d2, alternative='two-sided')
        elif AGGREGATION_FUNCTION == "mean":
            tstat, p = stats.ttest_ind(d1, d2, equal_var=False)
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