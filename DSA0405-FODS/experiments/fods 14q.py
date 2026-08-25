import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Age": [21, 25, 21, 30, 25, 28, 30, 21, 35, 25]
})

frequency = df["Age"].value_counts().sort_index()

print("Frequency Distribution of Customer Ages:")
print(frequency)
