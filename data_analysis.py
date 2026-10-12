
# Hands-On Data Lab Implementation

import pandas as pd

# Sample student data
data = {
    "Name": ["Ravi", "Sita", "Ram", "Priya", "Kiran"],
    "Marks": [85, 90, 75, 95, 80]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display student data
print("Student Marks Data:")
print(df)

# Calculate average marks
average = df["Marks"].mean()
print("\nAverage Marks:", average)

# Find the highest marks
print("Highest Marks:", df["Marks"].max())

# Find the lowest marks
print("Lowest Marks:", df["Marks"].min())
