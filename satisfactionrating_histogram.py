import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
data_set = pd.read_csv("updated_cleaned_dataset1.csv")

# Create histogram of SatisfactionRating
plt.figure(figsize=(10, 6))  # Set figure size
plt.hist(data_set["SatisfactionRating"], bins=20, color='red', edgecolor='black')  # Create histogram
plt.title("Distribution of Satisfaction Rating")  # Set title
plt.xlabel("Satisfaction Rating")  # Set x-axis label
plt.ylabel("Frequency")  # Set y-axis label
plt.savefig("distribution_of_satisfaction_histogram.png")  # Save plot
plt.show()  # Display plot
