import pandas as pd
import itertools
import numpy as np
from scipy import stats
from statsmodels.stats.multitest import multipletests

from SETTINGS import alpha


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

