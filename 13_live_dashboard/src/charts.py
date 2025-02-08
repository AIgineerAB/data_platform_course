import matplotlib.pyplot as plt


def line_chart(x, y, **options):
    fig, ax = plt.subplots(1)

    ax.plot(x, y, linewidth=3)

    ax.set(
        title=options.get("title"),
        xlabel=options.get("xlabel"),
        ylabel=options.get("ylabel"),
    )

    fig.tight_layout()
    return fig