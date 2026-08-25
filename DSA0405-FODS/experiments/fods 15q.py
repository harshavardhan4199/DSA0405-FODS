import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Likes": [100, 200, 100, 300, 200, 100, 400, 300, 200, 100]
})

frequency = df["Likes"].value_counts().sort_index()

print("Frequency Distribution of Likes:")
print(frequency)
