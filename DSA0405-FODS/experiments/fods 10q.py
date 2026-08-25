import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sales_data.csv")

monthly_sales = df.groupby("Month_sales")["Price"].sum()

# Line graph
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=60)
plt.show()

# Bar graph
plt.bar(monthly_sales.index, monthly_sales.values)
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=60)
plt.show()
