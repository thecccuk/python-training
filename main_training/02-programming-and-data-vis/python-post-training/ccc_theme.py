"""
The CCC chart theme, as used on the course.

This is a standalone copy of `jrpyvis.ccc_theme` for the post-training
exercises, which run without the course package installed. On the course you
applied the theme with

    import jrpyvis.ccc_theme as ccc

and here you do the same thing with

    import ccc_theme as ccc

as long as this file sits next to your notebook. Everything else is the same:
importing it applies the theme, and it gives you `Colors`, `SCENARIO_COLORS`
and `zero_line()`.

If you change this file, change `jrpyvis/ccc_theme.py` to match.
"""

import matplotlib.pyplot as plt
from cycler import cycler

from pathlib import Path
from matplotlib import font_manager


# The CCC's charts use the proprietary Century Gothic; we instead use URW Gothic,
# a free look-alike shipped in the fonts/ folder next to this file. If that
# folder is missing, matplotlib falls back to its default font and the charts
# still work.
_FONT_DIR = Path(__file__).resolve().parent / "fonts"
if _FONT_DIR.is_dir():
    for _font in _FONT_DIR.iterdir():
        if _font.name.endswith(".otf"):
            font_manager.fontManager.addfont(str(_font))


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
plt.rcParams["font.family"] = ["URW Gothic", "DejaVu Sans"]

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
