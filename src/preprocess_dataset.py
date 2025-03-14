import re
import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv("fake_transactions.csv")

# Convert text to lowercase & remove special characters
df["Transaction_Description"] = df["Transaction_Description"].str.lower()
df["Transaction_Description"] = df["Transaction_Description"].apply(lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", x))

# Handle missing values (fill with "Unknown")
df.fillna({"Transaction_Description": "unknown", "Amount": df["Amount"].median()}, inplace=True)

# Remove extreme outliers (any amount > $50,000)
df = df[df["Amount"] < 50000]

# Save cleaned dataset
df.to_csv("cleaned_fake_transactions.csv", index=False)

print("Preprocessing complete!")
