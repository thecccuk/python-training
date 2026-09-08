"""Functions for plotting"""

import matplotlib.pyplot as plt


def plot_total_emissions(
    data,
    sector,
    units="GtCO2eq",
    output_filename="emissions.png"
):
    """Plots total emissions against year

    Parameters
    ----------
    data: pd.DataFrame
      Data set including `total_emissions`, `total_emissions_gt`
      and `year` columns
    sector: str
      Sector that is being plotted
    units: str
      Units label for the emissions axis ("GtCO2eq" by default)
    output_filename: str
      Name of the output image file ("emissions.png" by default)
    """
    if units == "GtCO2eq":
        total_emissions = data["total_emissions_gt"]
    elif units == "MtCO2eq":
        total_emissions = data["total_emissions"]
    else:
        raise ValueError(
            "'units' should be 'GtCO2eq' or 'MtCO2eq'"
        )
    plt.scatter(
        data["year"], total_emissions
    )
    plt.title(f"Projected emissions for {sector}")
    plt.xlabel("Year")
    plt.ylabel(f"Total emissions [{units}]")
    plt.savefig(output_filename)
