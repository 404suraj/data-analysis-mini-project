import pandas as pd

data = {
    "Student": ["A", "B", "C", "D"],
    "Marks": [78, 85, 69, 90]
}

df = pd.DataFrame(data)

print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())