import pandas as pd
import re
from collections import Counter

df = pd.DataFrame({
    "Review": [
        "Good product and good quality",
        "Excellent product and fast delivery",
        "Good quality product",
        "Excellent quality"
    ]
})

text = " ".join(df["Review"].astype(str))

words = re.findall(r'\b\w+\b', text.lower())

frequency = Counter(words)

print("Word Frequency Distribution:")
for word, count in frequency.items():
    print(word, ":", count)
