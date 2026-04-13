
from statsmodels.stats.anova import anova_lm
# import scikit_posthocs as sp
import pandas as pd
import networkx as nx




def compact_letter_display(groups, n, sig_matrix, print_info:bool=True):
    # Graph bauen: Kante = keine signifikante Differenz
    if groups is None:
        return None
    G = nx.Graph()
    G.add_nodes_from(groups)
    for i in range(n):
        for j in range(i + 1, n):
            if sig_matrix[i, j]:
                G.add_edge(groups[i], groups[j])

    # Cliques als Gruppen gleicher Buchstaben
    cliques = list(nx.find_cliques(G))

    # Buchstaben zuteilen (einfach a,b,c,...)
    letters = []
    from string import ascii_lowercase
    letter_dict = dict()
    used = set()
    for i, group in enumerate(groups):
        letter_dict[group] = set()
    for i, clique in enumerate(cliques):
        letter = ascii_lowercase[i]
        for g in clique:
            letter_dict[g].add(letter)

    # Ausgabe als String mit zusammengefassten Buchstaben pro Gruppe
    cld_strings = {g: ''.join(sorted(letters)) for g, letters in letter_dict.items()}

    if print_info:
        print("\nCompact Letter Display:")
        for g in sorted(cld_strings):
            print(f"{g}: {cld_strings[g]}")
    return cld_strings