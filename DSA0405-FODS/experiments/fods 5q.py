import numpy as np

# Load the CSV file
fuel_data = np.genfromtxt(
    "Fuel_data.csv",
    delimiter=",",
    skip_header=1,
    dtype=str
)

# Extract columns
make = fuel_data[:, 1]                  # Make column
fuel_efficiency = fuel_data[:, 7].astype(float)   # FuelEfficiency column

# Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Separate Mazda and Audi fuel efficiencies
mazda_eff = fuel_efficiency[make == "Mazda"]
audi_eff = fuel_efficiency[make == "Audi"]

# Calculate averages
mazda_avg = np.mean(mazda_eff)
audi_avg = np.mean(audi_eff)

# Percentage improvement
percentage_improvement = ((mazda_avg - audi_avg) / audi_avg) * 100

# Display results
print("Average Fuel Efficiency of all cars:", round(average_efficiency, 2), "MPG")
print("Average Fuel Efficiency of Mazda:", round(mazda_avg, 2), "MPG")
print("Average Fuel Efficiency of Audi:", round(audi_avg, 2), "MPG")
print("Percentage Improvement from Mazda to Audi:", round(percentage_improvement, 2), "%")
