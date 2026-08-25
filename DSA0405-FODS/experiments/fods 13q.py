from collections import Counter
import re

with open("sample_text.txt", "r") as file:
    text = file.read()

words = re.findall(r'\b\w+\b', text.lower())

frequency = Counter(words)

print("Word Frequency Distribution:")
for word, count in frequency.items():
    print(word, ":", count)
