from utils.data import (
    clean_data,
    convert_to_gigatonnes,
    load_data,
)
from utils.plotting import plot_total_emissions

# Load raw data
data = load_data()

# Clean and preprocess the data
data = clean_data(data)
data = convert_to_gigatonnes(data)

# Plot the data
plot_total_emissions(data=data, sector="aviation")
