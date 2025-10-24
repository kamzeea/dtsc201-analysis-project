import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
data_set = pd.read_csv("updated_cleaned_dataset1.csv")

# Calculate mean satisfaction rating by student level
satisfaction_by_level = data_set.groupby("StudentLevel")["SatisfactionRating"].mean()


# Create bar chart of SatisfactionRating by StudentLevel
plt.figure(figsize=(10, 6))  # Set figure size
bars = plt.bar(satisfaction_by_level.index, satisfaction_by_level.values, 
               color=["#36A2EB", "#FF6384", "#FFCE56", "#4BC0C0"])  # Create bar chart

# Add value labels on top of each bar
for bar in bars:
    yval = bar.get_height()  # Get the height of the bar
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, f'{yval:.2f}', 
             ha='center', va='bottom', fontsize=10)  # Add text above bar
plt.title("Satisfaction Rating by Student Level")  # Set title
plt.xlabel("Student Level")  # Set x-axis label
plt.ylabel("Satisfaction Rating")  # Set y-axis label
plt.savefig("satisfactionratigbystudentlevel_barplot.png")  # Save plot
plt.show()  # Display plot
