import numpy as np

house_data = np.loadtxt(
    "House_data.csv",
    delimiter=",",
    skiprows=1,
    usecols=(1, 2, 3, 5)
)

houses_more_than_4 = house_data[house_data[:, 0] > 4]

average_price = np.mean(houses_more_than_4[:, 3])

print("Average price of houses with more than 4 bedrooms:",
      round(average_price, 2))
