import numpy as np

sales_data = np.genfromtxt(
    "Sales_data.csv",
    delimiter=",",
    skip_header=1,
    dtype=str
)

months = sales_data[:, 1]
sales = sales_data[:, 4].astype(float)

Q1 = 0.0
Q4 = 0.0

for i in range(len(months)):
    if (months[i] == "January" or
        months[i] == "February" or
        months[i] == "March"):
        Q1 += sales[i]

    elif (months[i] == "October" or
          months[i] == "November" or
          months[i] == "December"):
        Q4 += sales[i]

total_sales_year = np.sum(sales)

percentage_increase = ((Q4 - Q1) / Q1) * 100

print("Total sales for the year:",
      round(total_sales_year, 2))

print("Percentage increase from Q1 to Q4:",
      round(percentage_increase, 2), "%")
