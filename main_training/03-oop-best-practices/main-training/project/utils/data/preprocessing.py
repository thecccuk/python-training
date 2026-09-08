"""Functions for dealing with data preprocessing, including

- data cleaning operations;
- unit conversions.
"""


def clean_data(data):
    """Remove missing values and clean up variable names

    :parameters:
    data: pd.DataFrame
      Pandas DataFrame with the data to be cleaned

    :returns:
    pd.DataFrame object with the tidy data
    """
    data.dropna(inplace=True)
    return data


def convert_to_gigatonnes(data):
    """Converts total_emissions column from MtCO2eq to GtCO2eq

    Parameters
    ----------
    data: pd.DataFrame
      Data set that includes a `total_emissions` column

    Returns
    -------
    pd.DataFrame
      Same data set with an additional `total_emissions_gt`
      column in GtCO2eq units
    """
    data["total_emissions_gt"] = (
        data["total_emissions"] / 1000
    )
    return data
