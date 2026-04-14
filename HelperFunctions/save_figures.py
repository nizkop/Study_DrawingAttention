import numpy as np


def save_figures(fig, axes, title:str, bbox_extra_artists:list=[]):
    # TODO format plot and axis
    if not isinstance(axes, list) and not isinstance(axes, np.ndarray):
        axes = [axes]
    for ax in axes:
        ax.grid(True, axis='y', linestyle='--', alpha=0.7)
        fig.tight_layout()

    title = title.replace(".pdf","").replace(".png","")

    fig.savefig(f"results/{title}.pdf", bbox_inches="tight", bbox_extra_artists=bbox_extra_artists )
    fig.savefig(f"results/{title}.png", bbox_inches="tight", bbox_extra_artists=bbox_extra_artists )