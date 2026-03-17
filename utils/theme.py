import matplotlib.pyplot as plt
from cycler import cycler

Colors = {
    "vibrant purple": "#7041FF",
    "orange": "#FFAC00",
    "aubergine": "#280049",
    "lavender": "#8C57CC",
    "purple 4": "#AB6B99",
    "purple 5": "#CA7880",
    "red": "#FF2200",
    "yellow": "#FFFF4B",
    "green": "#A2D800",
    "forest green": "#1A5F31",
    "sea green": "#369992",
    "sky blue": "#AEC5EB",
}

# set default colours to use
plt.rcParams["axes.prop_cycle"] = cycler(color=list(Colors.values()))

# style plots to match CCC branding
plt.rcParams["figure.figsize"] = [6, 3]
plt.rcParams["figure.constrained_layout.use"] = True
plt.rcParams["figure.dpi"] = 120
plt.rcParams["axes.grid"] = True
plt.rcParams["axes.grid.axis"] = "y"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["axes.titlecolor"] = Colors["vibrant purple"]
plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.labelcolor"] = Colors["vibrant purple"]
plt.rcParams["axes.edgecolor"] = Colors["vibrant purple"]
plt.rcParams["axes.spines.left"] = False
plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["grid.linewidth"] = 0.4
plt.rcParams["grid.color"] = "silver"
plt.rcParams["xtick.color"] = Colors["vibrant purple"]
plt.rcParams["ytick.color"] = Colors["vibrant purple"]
plt.rcParams["ytick.left"] = False
plt.rcParams["legend.frameon"] = False
plt.rcParams["legend.labelcolor"] = Colors["vibrant purple"]
plt.rcParams["font.family"] = "century gothic"

SCENARIO_COLORS = {
    "Baseline": Colors["orange"],
    "Pathway": Colors["vibrant purple"],
    "Historical": Colors["aubergine"],
}


def zero_line(ax, hide_bottom_spine=False):
    # Get the bottom spine for styling reference
    spine = ax.spines["bottom"]
    spine.set_position(("data", 0))

    # Draw the zero line with the spine's properties
    ax.axhline(
        0,
        color=spine.get_edgecolor(),
        linewidth=spine.get_linewidth(),
        linestyle=spine.get_linestyle(),
        zorder=0  # put behind data (optional)
    )

    # Optionally hide the bottom spine afterwards
    if hide_bottom_spine:
        ax.spines["bottom"].set_visible(False)
