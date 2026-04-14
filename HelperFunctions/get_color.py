from SETTINGS import COLORS


def get_color(label:str):
    if label not in COLORS:
        return COLORS["DEFAULT"]
    return COLORS[label]