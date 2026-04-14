import warnings


def get_partial_ETA_squared(anova_result):
    """
    eta = [(F Value) * (Num Df)] / [(F Value) * (Num Df) + (Den DF)]
    :param anova_result:
    :return:
    """
    with warnings.catch_warnings(record=True) as w:
        warnings.filterwarnings("always", category=RuntimeWarning)
        f = anova_result.anova_table["F Value"].iloc[-1]
        df_effect = anova_result.anova_table['Num DF'].iloc[-1]
        df_error = anova_result.anova_table["Den DF"].iloc[-1]
        return (f * df_effect ) / (f * df_effect + df_error)
