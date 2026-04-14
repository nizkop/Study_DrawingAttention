

def save_figures(fig, ax, title:str):
    # TODO format plot and axis

    title = title.replace(".pdf","").replace(".png","")

    fig.savefig(f"results/{title}.pdf", bbox_inches="tight")
    fig.savefig(f"results/{title}.png", bbox_inches="tight")