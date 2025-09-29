import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
df = pd.read_csv('cleaned_dataset.csv')

# Histogram of SessionLengthMin
plt.figure(figsize=(8, 6))
#plt.hist(df["SessionLengthMin"], bin =15, edgecolor='green')
sns.histplot(df["SessionLengthMin"], bins=20, color="green")
plt.title("Distribution of AI Session Length")
plt.xlabel("Session Length (Minutes)")
plt.ylabel("Count")
plt.savefig("session_length_histogram.png")
plt.show()
