import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("phone_numbers.csv")

# Example: Create a bar chart of call status
status_counts = df["Status"].value_counts()
plt.bar(status_counts.index, status_counts.values)
plt.xlabel("Call Status")
plt.ylabel("Count")
plt.title("Call Status Distribution")
plt.show()
